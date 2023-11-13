Welcome!

This file is meant to guide you on how to use the Jupyter notebook in which
our workflow is implemented.

*************************************
Additional files required.
*************************************

Since we integrated external data into our the provided data, our code requires
some additional data files. The required files are:

met_data_clean.pkl - Pandas dataframe stored in a .pkl format, containing past
                    measurements of weather data.

stations_df_clean.pkl - Pandas dataframe stored in a .pkl format, containing
the information of approximately 300 weather stations around the U.S.

states_parks.csv - .csv table containing data regarding the number of parks
in each state in the U.S.

units_try.csv - example .csv table, containing all the data in
'NWCG_UnitIDActive_20170109' (further details provided soon). This table
demonstrates an example of how the units data should be formatted.

Those files can be found in the following link:

https://drive.google.com/drive/folders/1ZY3o190w7mjXHIr2n_QXgOj1iv4hnlqP?usp=sharing

*************************************
Submission files
*************************************
In the submission box, you should find the following files:

project_190223.ipynb - The main notebook, in which the entire workflow is
                      implemented.

meteoStatTry.ipynb - Additional notebook, in which the process of fetching
                    the weather data is implemented. The code in this notebook
                    is not required for running the main notebook

cause_stats.py - external .py script used for computing 'prior' values. (further
                information can be found in the report)

README - this file

requirements.txt - requirements file

*************************************
User manual + important notes
*************************************
The code in the main notebook (project_190223.ipynb) allows you to provide
it with train and test data sets, and should be able to process them smoothly.

In order for that to happen, please meet the following requirements:
1. All provided data files should be in a .csv format.

2. At the top of the main notebook, there is an option to provide the
file paths for the train set, test set, and units data (see section 3).
* important note - if the train path is set to None - then the notebook
will use the data originally provided: 'FPA_FOD_20170508.sqlite'. (please
make sure you include it in the same directory as the notebook)

3. In the provided data .sqlite file ('FPA_FOD_20170508.sqlite') there are 2
tables, used by us in the process: 'Fires' and 'NWCG_UnitIDActive_20170109'.
Therefore, our code requires a .csv table containing similar information, and
formatted in the same manner as the 'NWCG_UnitIDActive_20170109' table.
the units .csv should contain all the information regarding the units in the
train and tests sets. Much like in the 'NWCG_UnitIDActive_20170109' table.

4. The notebook code also allows you to choose whether to perform hyper-parameters
optimization. Please see documentation within the notebook.
