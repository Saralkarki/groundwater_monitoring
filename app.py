import dash
import dash_bootstrap_components as dbc




#external_stylesheets = ['assets/css/main.css','assets/css/user.css' ]
app = dash.Dash(__name__, external_stylesheets = [dbc.themes.JOURNAL])
app.config.suppress_callback_exceptions = True




# main div


