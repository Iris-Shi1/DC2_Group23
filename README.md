# DC2_Group23
imports: pandas 2.2.2, jupyter 1.0.0, seaborn  0.13.2, matplotlib 3.8.4, shapely 2.0.4, geopandas 1.0.0a1, xgboost 2.0.3, scikit-learn 1.5.0, openpyxl 3.1.4, lightgbm 4.4.0, imblearn 0.0, statsmodels 0.14.2, tqdm 4.66.4, numpy 1.26.4, scipy 1.13.1, folium 0.16.0, dash 2.17.0, dash-bootstrap-components 1.6.0, dash-core-components 2.0.0, dash-html-components 2.0.0, dash-table 5.0.0  
DC2group23

Before running the code, make sure the following files are added to your 'data' folder:
- all the data for crimes from 2010 to 2024. It is ok if it is in the form of folders separated by year and month. You can access the data for download from the police.uk data repository via this link: https://data.police.uk/data/

- PAS granular data. Please download numerical PAS granular data ('PAS_Numerical_Data_borough_valid.csv' and 'PAS_Numerical_Data_673.csv') before runing the code. You can access the data for download via this link: https://drive.google.com/drive/folders/1MUJVoi3LJgRYNnWxUnECAuLPlaBMn0zm

- London_Boroughs.gpkg - https://data.london.gov.uk/dataset/london_boroughs

In project data there is an already existing dataset named 'Data' since that dataset has been manually made in Excel.

Before running any of the EDA, models or visualization, first run the files in 'Dataset_preparation' in the following order:
1. Merge.py
2. Vivan's scrapnotes (1).ipynb
3. PAS_Iris.ipynb
3. Crime data preprocessing.ipynb
4. Create dataset.py
5. Data_cleaning_preprocessing.ipynb

After all the datasets needed are created or added to their folders, the rest of the code can be used

Folder 'EDA' contains different files with exploratory analysis of the raw data

Folder 'Model' contains deeper analysis of the data and the feature extraction models for the London as a whole as well as borough level.

Folder 'Statistical_testing' contains a file that tests using different methods the validity of the results in 'Model'.

Folder 'Visualizations' contains files in which the visualizations of the results can be obtained