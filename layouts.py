
import dash_core_components as dcc
import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx




from app import app

from options import tubewell_options, years_dict

# bermuda = dlx.dicts_to_geojson([dict(lat=32.299507, lon=-64.790337)])

def get_info(feature=None):
    header = [html.H4("Tubewell in Banke District")]
    if not feature:
        return header + ["Mouse over an area"]
    return header + [html.B(f"Location: {feature['properties']['Location ']}"), html.Br(),
    html.B(f"Well No: {feature['properties']['Well No.']}")]

# Create info control.
info = html.Div(children=get_info(), id="info", className="info",style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "1000"})

app.title = 'Groundwater Monitoring'
main_layout = html.Div(
    [
# header div
        html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/cimmyt-logo.png', className = 'logo_cimmyt'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
#main body
        html.Div([
            # sidebar
            html.Div([
                dcc.Checklist(id = 'Tubewell_type', options = tubewell_options, 
                value = [], labelStyle={'display': 'inline-block'},
                ),
                html.Div(id = 'gw_map'),
                dl.Map(center=[28.05,81.61], zoom=10, children=[dl.TileLayer(), dl.GeoJSON(id = "gwt"), info]),
                #  html.Div(id = 'Test'),
                 

                # dcc.Dropdown(id = 'Taubewell_type',
                # options=tubewell_options,
                #         searchable=False,
                #         value='both',
                #         placeholder = "select a tubewell type",
                #         style = {'width': '95%', 'margin': '10px'},
                #         clearable=False
                # ),
                # Tubewells (This list will change as per the above selection)
                # dcc.Dropdown(id = 'Tubewell_location',
                # # options= st_location_options,
                #         searchable=False,
                #         value='',
                #         placeholder = "Select Tubewell region",
                #         style = {'width': '95%', 'margin': '10px'},
                # ),
                # html.H5("Date picker"),
                # html.H5("time picker"),
                # html.H5("actual value or average"),
                # html.H5("map view"),
                # html.H5("visualization view"),
                

            ], className = 'six columns sidebar offset-by-one'),
            #main window
            html.Div([
                html.Div([html.H6("GroundWater Level")], className = 'graph_text'),
                dcc.Graph(id = 'timeseries_gw_data',style={'width': '100%', 'height': '500px', 'margin-top': "-15px"}),
                dcc.Slider(id='year-slider',value = 2015, min = 1996, max = 2015,marks=years_dict,step=None)
                #  dcc.Graph(id = 'test_1'),

            ],className = 'six columns main_window')    
# Main div      
        ], className = 'twelve columns')
# Main container      
    ], className = 'twelve columns'
)

