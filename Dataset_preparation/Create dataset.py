import pandas as pd

# Read the CSV files into pandas DataFrames
try:
    df_extra = pd.read_csv('../project_data/Data.csv', low_memory=False)
    df_crime = pd.read_csv('../project_data/crime_type_data.csv', low_memory=False)
    print("Files read successfully.")
except FileNotFoundError as e:
    print(f"File not found: {e}")
    raise
except pd.errors.EmptyDataError as e:
    print(f"No data: {e}")
    raise
except pd.errors.ParserError as e:
    print(f"Parse error: {e}")
    raise
except Exception as e:
    print(f"An error occurred: {e}")
    raise

# Verify that the required columns exist in both DataFrames
required_columns = ['Month_Number', 'Borough']

for col in required_columns:
    if col not in df_extra.columns:
        print(f"Column '{col}' not found in 'df_extra'")
    if col not in df_crime.columns:
        print(f"Column '{col}' not found in 'df_crime'")

# Ensure columns have the same data types
print("df_extra column types:")
print(df_extra[required_columns].dtypes)
print("df_crime column types:")
print(df_crime[required_columns].dtypes)

# Convert columns to the same data type if necessary
df_extra['Month_Number'] = df_extra['Month_Number'].astype(str)
df_crime['Month_Number'] = df_crime['Month_Number'].astype(str)
df_extra['Borough'] = df_extra['Borough'].astype(str)
df_crime['Borough'] = df_crime['Borough'].astype(str)

# Check for missing data in the columns used for merging
print("Missing values in df_extra:")
print(df_extra[required_columns].isnull().sum())
print("Missing values in df_crime:")
print(df_crime[required_columns].isnull().sum())

# Merge DataFrames on 'Month_Number' and 'Borough'
try:
    merged_df = pd.merge(df_extra, df_crime, on=['Month_Number', 'Borough'], how='inner')
    print("Merge successful")
except KeyError as e:
    print(f"Merge failed: {e}")
    raise
except Exception as e:
    print(f"An error occurred during merging: {e}")
    raise

# Inspect the merged DataFrame
print("Merged DataFrame head:")
print(merged_df.head())
print("Merged DataFrame info:")
print(merged_df.info())

# Save the merged DataFrame to a CSV file
try:
    merged_df.to_csv('../project_data/extra_crime_dataset.csv', index=False)
    print('Merged DataFrame saved to extra_crime_dataset.csv')
except PermissionError as e:
    print(f"Permission error: {e}")
    raise
except IOError as e:
    print(f"IO error: {e}")
    raise
except Exception as e:
    print(f"An error occurred while saving the CSV: {e}")
    raise


