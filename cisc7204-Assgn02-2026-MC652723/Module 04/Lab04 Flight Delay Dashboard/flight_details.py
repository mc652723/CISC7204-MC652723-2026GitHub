# Module 04 Lab 04 - Practice Exercise
# Change the dashboard title to "Flight Details Statistics Dashboard"
# with a font size of 35 and save the file as flight_details.py.
import os

import pandas as pd
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio

pio.templates["cisc7204"] = go.layout.Template(
    layout=dict(font=dict(size=16), title=dict(font=dict(size=18)),
                legend=dict(font=dict(size=9), itemsizing='constant')))
pio.templates.default = "plotly_white+cisc7204"

DATA_URL = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
            'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv')
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airline_data.csv')

airline_data = pd.read_csv(
    DATA_FILE if os.path.exists(DATA_FILE) else DATA_URL,
    encoding="ISO-8859-1",
    dtype={'Div1Airport': str, 'Div1TailNum': str,
           'Div2Airport': str, 'Div2TailNum': str})

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Flight Details Statistics Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 35}),
    html.Div(["Input Year: ",
              dcc.Input(id='input-year', value='2010', type='number',
                        style={'height': '35px', 'font-size': 30})],
             style={'font-size': 30}),
    html.Br(),
    html.Br(),
    html.Div([
        html.Div(dcc.Graph(id='carrier-plot'), style={'width': '50%'}),
        html.Div(dcc.Graph(id='weather-plot'), style={'width': '50%'})
    ], style={'display': 'flex'}),
    html.Div([
        html.Div(dcc.Graph(id='nas-plot'), style={'width': '50%'}),
        html.Div(dcc.Graph(id='security-plot'), style={'width': '50%'})
    ], style={'display': 'flex'}),
    html.Div(dcc.Graph(id='late-plot'), style={'width': '65%'})
], style={'backgroundColor': '#FFFFFF', 'minHeight': '100vh', 'padding': '10px'})


def compute_info(airline_data, entered_year):
    df = airline_data[airline_data['Year'] == int(entered_year)]
    avg_car = df.groupby(['Month', 'Reporting_Airline'])['CarrierDelay'].mean().reset_index()
    avg_weather = df.groupby(['Month', 'Reporting_Airline'])['WeatherDelay'].mean().reset_index()
    avg_NAS = df.groupby(['Month', 'Reporting_Airline'])['NASDelay'].mean().reset_index()
    avg_sec = df.groupby(['Month', 'Reporting_Airline'])['SecurityDelay'].mean().reset_index()
    avg_late = df.groupby(['Month', 'Reporting_Airline'])['LateAircraftDelay'].mean().reset_index()
    return avg_car, avg_weather, avg_NAS, avg_sec, avg_late


@app.callback([
    Output(component_id='carrier-plot', component_property='figure'),
    Output(component_id='weather-plot', component_property='figure'),
    Output(component_id='nas-plot', component_property='figure'),
    Output(component_id='security-plot', component_property='figure'),
    Output(component_id='late-plot', component_property='figure')
],
    Input(component_id='input-year', component_property='value'))
def get_graph(entered_year):
    avg_car, avg_weather, avg_NAS, avg_sec, avg_late = compute_info(airline_data, entered_year)

    carrier_fig = px.line(avg_car, x='Month', y='CarrierDelay', color='Reporting_Airline',
                          title='Average carrier delay time (minutes) by airline')
    weather_fig = px.line(avg_weather, x='Month', y='WeatherDelay', color='Reporting_Airline',
                          title='Average weather delay time (minutes) by airline')
    nas_fig = px.line(avg_NAS, x='Month', y='NASDelay', color='Reporting_Airline',
                      title='Average NAS delay time (minutes) by airline')
    sec_fig = px.line(avg_sec, x='Month', y='SecurityDelay', color='Reporting_Airline',
                      title='Average security delay time (minutes) by airline')
    late_fig = px.line(avg_late, x='Month', y='LateAircraftDelay', color='Reporting_Airline',
                       title='Average late aircraft delay time (minutes) by airline')

    return [carrier_fig, weather_fig, nas_fig, sec_fig, late_fig]


if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('DASH_PORT', 8056)))
