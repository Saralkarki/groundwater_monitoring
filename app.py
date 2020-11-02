import dash

app = dash.Dash(__name__, suppress_callback_exceptions=True)
server = app.server

external_stylesheets = ['assets/css/main.css','assets/css/user.css' ]



# main div


