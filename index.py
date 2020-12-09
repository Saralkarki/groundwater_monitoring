import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

import dash_auth

from app import app
from layouts import main_layout, pilot_layout
import callbacks

VALID_USERNAME_PASSWORD_PAIRS = {
    'admin': 'admin@123',
    'administrator': 'admin@123'
}



server = app.server

auth = dash_auth.BasicAuth(
    app,
    VALID_USERNAME_PASSWORD_PAIRS
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])
# print(app.layout)


@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return main_layout
    elif pathname == '/pilot':
        return pilot_layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True, port = 8888)