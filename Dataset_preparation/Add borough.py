import pandas as pd
from shapely.geometry import Point
from geopandas import GeoDataFrame
from tqdm import tqdm  # Import tqdm for progress bar

# Read London boroughs data
boroughs_df = pd.read_csv('project_data/london_boroughs.csv', low_memory=False)

# Convert the boroughs DataFrame to a GeoDataFrame
geometry = [Point(xy) for xy in zip(boroughs_df['x'], boroughs_df['y'])]
boroughs_gdf = GeoDataFrame(boroughs_df, geometry=geometry)

# Read combined crime data
crime_df = pd.read_csv('project_data/combined_crime.csv')

# Define a function to find the borough for given coordinates
def find_borough(latitude, longitude):
    point = Point(longitude, latitude)
    for idx, row in boroughs_gdf.iterrows():
        if point.within(row['geometry']):
            return row['borough']
    return None

# Apply the function to create a new column with borough information
# Use tqdm to display progress
tqdm.pandas()  # Enable tqdm for pandas
crime_df['borough'] = crime_df.progress_apply(lambda row: find_borough(row['Latitude'], row['Longitude']), axis=1)

# Save the updated DataFrame with the new column
crime_df.to_csv('project_data/combined_crime_with_borough.csv', index=False)
