import dash
from dash import html, dcc
from dash.dependencies import Input, Output
import pandas as pd
import os

app = dash.Dash(__name__)
app.title = "SmartSniff Dashboard"

app.layout = html.Div(style={'background': '#1e1e1e', 'color': 'white', 'padding': 20}, children=[
    html.H1("SmartSniff – Live Threat Dashboard"),
    html.P("Suspicious packet sizes (live)"),
    dcc.Interval(id='interval', interval=5000, n_intervals=0),
    dcc.Graph(id='graph')
])

@app.callback(
    Output('graph', 'figure'),
    [Input('interval', 'n_intervals')]
)
def update(n):
    path = 'logs/threat_log.csv'
    if os.path.exists(path):
        df = pd.read_csv(path)
        fig = {
            'data': [{
                'x': list(range(len(df))),
                'y': df['packet_size'],
                'type': 'bar',
                'name': 'Suspicious Packets',
                'marker': {'color': 'red'}
            }],
            'layout': {
                'title': 'Packet Size Alerts',
                'paper_bgcolor': '#1e1e1e',
                'plot_bgcolor': '#1e1e1e',
                'font': {'color': 'white'}
            }
        }
        return fig
    else:
        return {
            'data': [],
            'layout': {
                'title': 'No suspicious packets yet.',
                'paper_bgcolor': '#1e1e1e',
                'font': {'color': 'white'}
            }
        }

if __name__ == '__main__':
    app.run(debug=True)  


