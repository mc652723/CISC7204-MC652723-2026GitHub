# Module 05 Practice Project - Part 02: Creating Dashboards (Australia Wildfire)
import os

import pandas as pd
import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates["cisc7204"] = go.layout.Template(
    layout=dict(font=dict(size=13), title=dict(font=dict(size=14)),
                legend=dict(font=dict(size=11))))
pio.templates.default = "plotly_white+cisc7204"

# Create app
app = dash.Dash(__name__)

# Clear the layout and do not display exception till callback gets executed
app.config.suppress_callback_exceptions = True

# Read the wildfire data into pandas dataframe (local copy first, then the course URL)
DATA_URL = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
            'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/Historical_Wildfires.csv')
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'Historical_Wildfires.csv')

df = pd.read_csv(DATA_FILE if os.path.exists(DATA_FILE) else DATA_URL)

# Extract year and month from the date column
df['Month'] = pd.to_datetime(df['Date']).dt.month_name()   # used for the names of the months
df['Year'] = pd.to_datetime(df['Date']).dt.year

MONTHS = ['January', 'February', 'March', 'April', 'May', 'June',
          'July', 'August', 'September', 'October', 'November', 'December']

# Layout Section of Dash
app.layout = html.Div(children=[
    html.H1('Australia Wildfire Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 26}),

    # Outer division starts
    html.Div([
        # First inner division for the input components
        html.Div([
            html.H2('Select Region:', style={'margin-right': '2em'}),

            # Radio items to select the region
            dcc.RadioItems([
                {"label": "New South Wales", "value": "NSW"},
                {"label": "Northern Territory", "value": "NT"},
                {"label": "Queensland", "value": "QL"},
                {"label": "South Australia", "value": "SA"},
                {"label": "Tasmania", "value": "TA"},
                {"label": "Victoria", "value": "VI"},
                {"label": "Western Australia", "value": "WA"}
            ], value="NSW", id='region', inline=True),

            # Dropdown to select year
            html.Div([
                html.H2('Select Year:', style={'margin-right': '2em'}),
                dcc.Dropdown(df.Year.unique(), value=2005, id='year')
            ]),
        ]),

        # Second inner division for the two output graphs
        html.Div([
            html.Div([], id='plot1', style={'width': '40%'}),
            html.Div([], id='plot2', style={'width': '60%'})
        ], style={'display': 'flex'}),
    ])
], style={'backgroundColor': '#FFFFFF', 'minHeight': '100vh', 'padding': '10px'})


@app.callback([Output(component_id='plot1', component_property='children'),
               Output(component_id='plot2', component_property='children')],
              [Input(component_id='region', component_property='value'),
               Input(component_id='year', component_property='value')])
def reg_year_display(input_region, input_year):
    # Data
    region_data = df[df['Region'] == input_region]
    y_r_data = region_data[region_data['Year'] == input_year]

    # Plot one - Monthly Average Estimated Fire Area
    est_data = y_r_data.groupby('Month')['Estimated_fire_area'].mean().reset_index()
    est_data['Month'] = pd.Categorical(est_data['Month'], categories=MONTHS, ordered=True)
    est_data = est_data.sort_values('Month')
    pie_fig = px.pie(est_data, values='Estimated_fire_area', names='Month',
                     title="{} : Monthly Average Estimated Fire Area in year {}".format(
                         input_region, input_year))
    pie_fig.update_traces(textposition='inside', textinfo='percent')
    fig1 = dcc.Graph(figure=pie_fig)

    # Plot two - Monthly Average Count of Pixels for Presumed Vegetation Fires
    veg_data = y_r_data.groupby('Month')['Count'].mean().reset_index()
    veg_data['Month'] = pd.Categorical(veg_data['Month'], categories=MONTHS, ordered=True)
    veg_data = veg_data.sort_values('Month')
    bar_fig = px.bar(veg_data, x='Month', y='Count',
                     title='{} : Average Count of Pixels for Presumed Vegetation Fires in year {}'.format(
                         input_region, input_year))
    bar_fig.update_xaxes(tickangle=-45, tickfont=dict(size=10))
    fig2 = dcc.Graph(figure=bar_fig)

    return [fig1, fig2]


if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('DASH_PORT', 8057)))
