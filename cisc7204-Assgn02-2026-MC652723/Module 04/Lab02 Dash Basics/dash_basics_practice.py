# Practice task for Module 04 Lab 02
# Change the dashboard title to "Airline On-time Performance Dashboard"
# and increase the font size from 40 to 50.
import os

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import dash
from dash import dcc
from dash import html

pio.templates["cisc7204"] = go.layout.Template(
    layout=dict(font=dict(size=16), title=dict(font=dict(size=18))))
pio.templates.default = "plotly_white+cisc7204"

DATA_URL = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
            'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv')
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airline_data.csv')

airline_data = pd.read_csv(
    DATA_FILE if os.path.exists(DATA_FILE) else DATA_URL,
    encoding="ISO-8859-1",
    dtype={'Div1Airport': str, 'Div1TailNum': str,
           'Div2Airport': str, 'Div2TailNum': str})

data = airline_data.sample(n=500, random_state=42)

fig = px.pie(data, values='Flights', names='DistanceGroup',
             title='Distance group proportion by flights')

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Airline On-time Performance Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 50}),
    html.P('Proportion of distance group (250 mile distance interval group) by flights.',
           style={'textAlign': 'center', 'color': '#F57241'}),
    dcc.Graph(figure=fig),
], style={'backgroundColor': '#FFFFFF', 'minHeight': '100vh', 'padding': '10px'})

if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('DASH_PORT', 8052)))
