# Module 04 Lab 03 - Practice Exercise: bar chart of flights to each destination state
import os

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

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

# Create a dash application
app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1('Total number of flights to the destination state split by reporting airline',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.Div(["Input Year: ",
              dcc.Input(id='input-year', value='2010', type='number',
                        style={'height': '50px', 'font-size': 35})],
             style={'font-size': 40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id='bar-plot'), style={'font-size': 35}),
], style={'backgroundColor': '#FFFFFF', 'minHeight': '100vh', 'padding': '10px'})


@app.callback(Output(component_id='bar-plot', component_property='figure'),
              Input(component_id='input-year', component_property='value'))
def get_graph(entered_year):
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # Total number of flights for each destination state / reporting airline combination
    bar_data = (df.groupby(['DestState', 'Reporting_Airline'])['Flights']
                  .sum()
                  .reset_index())

    fig = px.bar(bar_data, x='DestState', y='Flights', color='Reporting_Airline',
                 title='Total number of flights to the destination state split by reporting airline')
    fig.update_xaxes(tickangle=-45)
    return fig


if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('DASH_PORT', 8054)))
