import numpy.random
import pandas as pd
import numpy as np


def get_cause_stats_df(sub_sample_df: pd.DataFrame, second_level='UnitId'):
    unit_cause_df = sub_sample_df.groupby([second_level, 'STAT_CAUSE_DESCR']).count().iloc[:, 0]
    unit_count_df = sub_sample_df.groupby(second_level).count().iloc[:, 0]

    # normalize counts to proportions
    second_unique_vals = sub_sample_df[second_level].unique()
    cause_unique_vals = sub_sample_df['STAT_CAUSE_DESCR'].unique()

    for cause_val in cause_unique_vals:
        for second_val in second_unique_vals:
            try:
                unit_cause_df.loc[(second_val, cause_val)] = unit_cause_df.loc[(second_val, cause_val)] / \
                                                             unit_count_df.loc[second_val]
            except KeyError:
                continue

    # creating a data frame with the proportions
    res_df = pd.DataFrame(data=None, index=second_unique_vals, columns=cause_unique_vals)

    # filling the res df
    for second_val in second_unique_vals:
        for cause_val in cause_unique_vals:
            try:
                res_df.loc[second_val, cause_val] = unit_cause_df.loc[(second_val, cause_val)]
            except KeyError:
                res_df.loc[second_val, cause_val] = 0

    return res_df


def get_3level_cause_stats(sub_sample_df: pd.DataFrame, second_level='FIRE_YEAR', third_level='UnitId'):
    level_group = sub_sample_df.groupby([second_level, third_level, 'STAT_CAUSE_DESCR']).count().iloc[:, 0]
    level_count = sub_sample_df.groupby([second_level, third_level]).count().iloc[:, 0]

    # normalize counts to proportions
    for cur_index in level_group.index:
        cur_count_index = (cur_index[0], cur_index[1])
        level_group.loc[cur_index] = level_group.loc[cur_index] / level_count.loc[cur_count_index]

    # filling the result into a data frame
    res_df = []

    for second_val in sub_sample_df[second_level].unique():
        for third_val in sub_sample_df[third_level].unique():
            cur_row = {third_level: third_val,
                       second_level: second_val}

            for cause_val in sub_sample_df['STAT_CAUSE_DESCR'].unique():
                cur_group_index = (second_val, third_val, cause_val)

                try:
                    cur_fill_val = level_group.loc[cur_group_index]
                except KeyError:
                    cur_fill_val = 0

                cur_row.update({cause_val: cur_fill_val})

            res_df.append(cur_row)

    return pd.DataFrame(res_df)


def plug_3level_cause_stats(original_df: pd.DataFrame, stats_df: pd.DataFrame,
                            second_level='FIRE_YEAR', third_level='UnitId'):
    stats_df['merge_col'] = list(zip(stats_df[second_level], stats_df[third_level]))
    original_df['merge_col'] = list(zip(original_df[second_level], original_df[third_level]))

    new_stats_df = stats_df.drop([second_level, third_level], axis=1)

    original_df = original_df.merge(new_stats_df, how='left', on='merge_col')

    original_df.drop('merge_col', axis=1, inplace=True)
    stats_df.drop('merge_col', axis=1, inplace=True)

    return original_df
