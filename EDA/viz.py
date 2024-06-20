import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

# Load the data
data = pd.read_csv('project_data/combined_crime.csv', low_memory=False)

# Check the first few rows of data to ensure it loaded correctly
print("Loaded Data:")
print(data.head())

# Ensure the 'Month' column contains valid date strings
data['Month'] = pd.to_datetime(data['Month'], errors='coerce')

# Drop rows with invalid 'Month' values
data.dropna(subset=['Month'], inplace=True)

# Extract year from the 'Month' column
data['Year'] = data['Month'].dt.year

# Filter for shoplifting instances
shoplifting_data = data[data['Crime type'].str.strip().str.lower() == 'shoplifting']

# Initialize the Dash app
app = dash.Dash(__name__, external_stylesheets=['https://codepen.io/chriddyp/pen/bWLwgP.css'])

app.layout = html.Div([
    html.H1("Shoplifting Incidents in London"),
    dcc.Dropdown(
        id='year-dropdown',
        options=[{'label': str(year), 'value': year} for year in sorted(shoplifting_data['Year'].unique())],
        value=sorted(shoplifting_data['Year'].unique())[0],
        clearable=False
    ),
    dcc.Graph(id='map-graph')
])

@app.callback(
    Output('map-graph', 'figure'),
    Input('year-dropdown', 'value')
)
def update_map(selected_year):
    filtered_data = shoplifting_data[shoplifting_data['Year'] == selected_year]

    # Aggregate data by location
    agg_data = filtered_data.groupby(['Latitude', 'Longitude']).size().reset_index(name='count')

    fig = px.scatter_mapbox(
        agg_data,
        lat='Latitude',
        lon='Longitude',
        size='count',
        color_continuous_scale='Viridis',
        size_max=15,
        zoom=10,
        mapbox_style="carto-positron",
        title=f"Shoplifting Incidents in {selected_year}",
        labels={'count': 'Number of Incidents'}
    )

    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
