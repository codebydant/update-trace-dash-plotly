# Custom Dash Core Components - update traces
This is a library to update multiples traces in one graph using dash plotly in python. This code is based from the "mydcc.Change_trace", repo: https://github.com/jimmybow/mydcc 

## Installation: 
    1. installing:
    ```
    $ pip install dash_update_data_components
    ```
## Requirements:
* **dash** -- The core dash backend
* **dash-renderer** -- The dash front-end
* **dash-html-components** -- HTML components
* **dash-core-components** -- Supercharged components
* **plotly** -- Plotly graphing library used in examples

## Example:
```
import dash_update_data_components

app.layout = html.Div([
    html.Div(children=[
        dcc.Graph(
              id='mainGraph',
              figure={
                  'data': data,
                  'layout': layout          
        )
    ]),

    dash_update_data_components.EditableGraph(id = 'ii', aim = 'mainGraph'),
])

# Callback button: change color
@app.callback(dash.dependencies.Output(component_id='ii', component_property='data'),             
             [dash.dependencies.Input(component_id='mainGraph', component_property='figure')])
def update_graph(fig):
    if fig is not None:        
        data = dict(x = fig['data'][0]['x']+20,
                    y = fig['data'][0]['y']-20,
                    opacity = 1
                    )

        return [data]
    else:
        raise PreventUpdate

if __name__ == '__main__':
    app.run_server(debug=True)
```

## Test:

    1.  Run the `usage.py` sample dash app:
        ```
        $ python usage.py
        ```

<img src="example.png" align="center" height="600" width="900"><br>

