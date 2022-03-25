import dash
from dash import Dash, dcc, html
import pandas

app = Dash()
app.layout = html.Div(
    [
        html.Div(html.H1("Accenture Project")),
        html.Div(
            dcc.Dropdown(
                id="mydropdown",
                options=[
                    {"label": "New York", "value": "New York"},
                    {"label": "San Francisco", "value": "San Francisco"},
                ],
            )
        ),
    ]
)


app.run_server(debug=True)
