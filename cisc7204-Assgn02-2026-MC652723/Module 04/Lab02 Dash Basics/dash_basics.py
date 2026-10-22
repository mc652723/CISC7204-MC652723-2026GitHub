# Import required packages
import os

import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.io as pio
import dash
from dash import dcc
from dash import html

# Larger, consistent chart typography so screenshots stay legible when scaled
pio.templates["cisc7204"] = go.layout.Template(
    layout=dict(font=dict(size=16), title=dict(font=dict(size=18))))
pio.templates.default = "plotly_white+cisc7204"

# Read the airline data into pandas dataframe (local copy first, then the course URL)
DATA_URL = ('https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/'
            'IBMDeveloperSkillsNetwork-DV0101EN-SkillsNetwork/Data%20Files/airline_data.csv')
DATA_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'airline_data.csv')

airline_data = pd.read_csv(
    DATA_FILE if os.path.exists(DATA_FILE) else DATA_URL,
    encoding="ISO-8859-1",
    dtype={'Div1Airport': str, 'Div1TailNum': str,
           'Div2Airport': str, 'Div2TailNum': str})

# Randomly sample 500 data points. Setting the random state to be 42 so that we get same result.
data = airline_data.sample(n=500, random_state=42)

# Pie Chart Creation
fig = px.pie(data, values='Flights', names='DistanceGroup',
             title='Distance group proportion by flights')

# Create a dash application
app = dash.Dash(__name__)

# Get the layout of the application and adjust it.
# Create an outer division using html.Div and add title to the dashboard using html.H1 component
# Add description about the graph using HTML P (paragraph) component
# Finally, add graph component.
app.layout = html.Div(children=[
    html.H1('Airline Dashboard',
            style={'textAlign': 'center', 'color': '#503D36', 'font-size': 40}),
    html.P('Proportion of distance group (250 mile distance interval group) by flights.',
           style={'textAlign': 'center', 'color': '#F57241'}),
    dcc.Graph(figure=fig),
], style={'backgroundColor': '#FFFFFF', 'minHeight': '100vh', 'padding': '10px'})

# Run the application
if __name__ == '__main__':
    app.run(debug=False, port=int(os.environ.get('DASH_PORT', 8051)))
