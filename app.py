import dash


external_stylesheets = ['assets/css/main.css','assets/css/user.css' ]
app = dash.Dash(__name__, external_stylesheets = external_stylesheets)
app.config.suppress_callback_exceptions = True




# main div


