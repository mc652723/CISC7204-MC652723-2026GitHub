# Module 04 Lab 03 - Add Interactivity: User Input and Callbacks
import os

import pandas as pd
import plotly.graph_objects as go
import plotly.io as pio
import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output

pio.templates["cisc7204"] = go.layout.Template(
    layout=dict(font=dict(size=16), title=dict(font=dict(size=18))))
pio.templates.default = "plotly_white+cisc7204"

# Read the airline data into the pandas dataframe
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
    html.H1('Airline Performance Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.Div(["Input Year: ",
              dcc.Input(id='input-year', value='2010', type='number',
                        style={'height': '50px', 'font-size': 35})],
             style={'font-size': 40}),
    html.Br(),
    html.Br(),
    html.Div(dcc.Graph(id='line-plot')),
], style={'backgroundColor': '#FFFFFF', 'minHeight': '100vh', 'padding': '10px'})


# Add callback decorator
@app.callback(Output(component_id='line-plot', component_property='figure'),
              Input(component_id='input-year', component_property='value'))
# Add computation to callback function and return graph
def get_graph(entered_year):
    # Select data by the entered year
    df = airline_data[airline_data['Year'] == int(entered_year)]

    # Group the data by Month and compute the average over arrival delay time.
    line_data = df.groupby('Month')['ArrDelay'].mean().reset_index()

    fig = go.Figure(data=go.Scatter(x=line_data['Month'], y=line_data['ArrDelay'],
                                    mode='lines', marker=dict(color='green')))
    fig.update_layout(title='Month vs Average Flight Delay Time',
                      xaxis_title='Month', yaxis_title='ArrDelay')
    return fig


# Run the app
if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('DASH_PORT', 8053)))
