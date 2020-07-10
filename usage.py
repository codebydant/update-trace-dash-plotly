import dash_update_data_components

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate

import plotly
import plotly.graph_objects as go

import numpy as np
import random

# Randomic data
N = 100
random_x = np.linspace(0, 40, N)
random_y0 = np.random.randn(N) + 5
random_y1 = np.random.randn(N)
random_y2 = np.random.randn(N) - 5

# Plotly traces
trace = []
trace.append(go.Scatter(x=random_x, y=random_y0,line=dict(color='green', width=2),visible=True,showlegend=True,name='trace 1'))
trace.append(go.Scatter(x=random_x, y=random_y1,line=dict(color='yellow', width=2),visible=True,showlegend=True,name='trace 2'))
traces = [trace]

# Data
data = [val for sublist in traces for val in sublist]

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# App: body
app.layout = html.Div([
    html.Div(children=[
        dcc.Graph(
              id='mainGraph',
              figure={
                  'data': data,
                  'layout': {
                      'xaxis': {
                          'autorange': True,
                          'showline': False,
                          'showticklabels': True,
                      },
                      'yaxis': {
                          'autorange': True,
                          'scaleanchor': 'x',
                          'scaleratio': 1,
                          'showline': False,
                          'showticklabels': True,
                      },
                      'height': 500,
                      'width': 1250,
                  },
            },
          config={
          'editable': False,
          'displayModeBar': True,
          'scrollZoom': False
          }
      )
    ]),

    # Custom dash component to update data in a dcc.Graph
    dash_update_data_components.EditableGraph(id = 'ii', aim = 'mainGraph'),

    # Button - change color
    html.Div(children=[html.Button('change color', id='button',n_clicks=0)]),
])

# Callback button: change color
@app.callback(dash.dependencies.Output(component_id='ii', component_property='data'),
             [dash.dependencies.Input(component_id='button', component_property='n_clicks')],
             [dash.dependencies.State(component_id='mainGraph', component_property='figure')])
def update_histogram(n_clicks, fig):
    if int(n_clicks) > 0:
        print("")
        new_style = []

        # alternate color between traces
        for prop_ in fig['data']:
            nam_ = prop_['name']
            if (nam_.find('trace 1') != -1):
                trace = prop_
                if(trace['line']['color']=='green'):
                    trace['line']['color']='yellow'
                else:
                    trace['line']['color']='green'
                new_style.append(dict(trace))
                continue
            else:
                trace = prop_
                if(trace['line']['color']=='green'):
                    trace['line']['color']='yellow'                    
                else:
                    trace['line']['color']='green'

                new_style.append(dict(trace))
                continue

        print("-----------------------")
        print("trace 1 color: ", new_style[0]['line']['color'])
        print("trace 2 color: ", new_style[1]['line']['color'])

        return new_style
    else:
        raise PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)
