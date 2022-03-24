import dash
from dash import dcc, html

app = dash.Dash()
app.layout = html.Div(
    [
        html.Div("Hello world with Dash"),
        html.H1("H1 tag here"),
        html.Div(
            dcc.Dropdown(
                id="my_drop_down_list",
                options=[
                    {"label": "New York", "value": "New York"},
                    {"label": "San Francisco", "value": "San Francisco"},
                ],
            )
        ),
    ]
)

app.run_server(debug=True)
