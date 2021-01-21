
import dash_core_components as dcc
import dash_table

import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx


from data_import import gw_df, banke_sw, banke_dw,bardiya_sw, bardiya_dw
import pandas as pd



from app import app

from options import tubewell_options, years_dict

# bermuda = dlx.dicts_to_geojson([dict(lat=32.299507, lon=-64.790337)])

def get_info(feature=None):
    header = [html.H4("Tubewell in Banke District")]
    if not feature:
        return header + ["Mouse over an area"]
    return header + [html.B(f"Location: {feature['properties']['Location ']}"), html.Br(),
    html.B(f"Well No: {feature['properties']['well_no']}")]

# Create info control.
info = html.Div(children=get_info(), id="info", className="info",style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "1000"})

app.title = 'Groundwater Monitoring'
pilot_layout = html.Div([
    html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Past-Database', href = '/historical_data', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),

        ],className = 'nav_bar'),
    html.Div([
         dcc.Link('Banke- Shallow Tube Well', href = '/pilot/bstw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Banke- Deep Tube Well', href = '/pilot/bdtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Shallow Tube Well', href = '/pilot/bastw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Deep Tube Well', href = '/pilot/badtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    ], style = {'background':'#fffccc'}),
    html.Br(),
    dash_table.DataTable(
    id='live_table',
    columns=[{"name": i, "id": i} for i in gw_df.columns],
     style_cell={
      
        'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
         
    },
    style_table={'overflowX': 'auto'},
    data=gw_df.to_dict('records'),
   
    export_format="csv",
),
dcc.Interval(
        id='interval_component',
        interval=60000,
        n_intervals=0
    )
], className = 'eleven columns offset-by-one')


main_layout = html.Div(
    [
# header div
        html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Past-Database', href = '/historical_data', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
        ],className = 'nav_bar'),
#main body
        html.Div([
            # sidebar
            html.Br(),
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
                # html.Div([ dcc.Slider(id='year-slider',value = 2015, min = 1996, max = 2015,marks=years_dict,step=None)], style = {'display':'none'}),
               
                #  dcc.Graph(id = 'test_1'),

            ],className = 'six columns main_window')    
# Main div      
        ], className = 'twelve columns')
# Main container      
    ], className = 'twelve columns'
)

################
####################Historical data######################

history_layout = html.Div(
    [
# header div
        html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Past-Database', href = '/historical_data', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),

        ],className = 'nav_bar'),
#main body
        html.Div([
            # sidebar
            html.Br(),
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
                dcc.Graph(id = 'timeseries_historical_data',style={'width': '100%', 'height': '500px', 'margin-top': "-15px"}),
                html.Div([ dcc.Slider(id='year-slider',value = 2015, min = 1996, max = 2015,marks=years_dict,step=None)]),
               
                #  dcc.Graph(id = 'test_1'),

            ],className = 'six columns main_window')    
# Main div      
        ], className = 'twelve columns')
# Main container      
    ], className = 'twelve columns'
)




###########################################
banke_stw_layout = html.Div([
    html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
        ],className = 'nav_bar'),
    html.Div([
        dcc.Link('All Data', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),

         dcc.Link('Banke- Shallow Tube Well', href = '/pilot/bstw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Banke- Deep Tube Well', href = '/pilot/bdtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Shallow Tube Well', href = '/pilot/bastw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Deep Tube Well', href = '/pilot/badtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    ], style = {'background':'#fffccc'}),
    html.Br(),
    dash_table.DataTable(
    id='live_table_banke_stw',
    columns=[{"name": i, "id": i} for i in banke_sw.columns],
    style_cell={
      
        'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
         
    },
    style_table={'overflowX': 'auto'},
    data=banke_sw.to_dict('records'),
   
    export_format="csv",
),
dcc.Interval(
        id='interval_component',
        interval=60000,
        n_intervals=0
    )
], className = 'eleven columns offset-by-one')

### Banke Deep deep well layout

banke_dtw_layout = html.Div([
    html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
        ],className = 'nav_bar'),
    html.Div([
    dcc.Link('All Data', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Banke- Shallow Tube Well', href = '/pilot/bstw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Banke- Deep Tube Well', href = '/pilot/bdtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Shallow Tube Well', href = '/pilot/bastw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Deep Tube Well', href = '/pilot/badtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    ], style = {'background':'#fffccc'}),
    html.Br(),
    dash_table.DataTable(
    id='live_table_banke_dtw',
    columns=[{"name": i, "id": i} for i in banke_dw.columns],
    style_cell={
      
        'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
         
    },
    style_table={'overflowX': 'auto'},
    data=banke_dw.to_dict('records'),
   
    export_format="csv",
),
dcc.Interval(
        id='interval_component',
        interval=60000,
        n_intervals=0
    )
], className = 'eleven columns offset-by-one')

### Bardiya Shallow well layout

bardiya_stw_layout = html.Div([
    html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
        ],className = 'nav_bar'),
    html.Div([
        dcc.Link('All Data', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),      
         dcc.Link('Banke- Shallow Tube Well', href = '/pilot/bstw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Banke- Deep Tube Well', href = '/pilot/bdtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Shallow Tube Well', href = '/pilot/bastw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Deep Tube Well', href = '/pilot/badtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    ], style = {'background':'#fffccc'}),
    html.Br(),
    dash_table.DataTable(
    id='live_table_bardiya_stw',
    columns=[{"name": i, "id": i} for i in bardiya_sw.columns],
    style_cell={
      
        'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
         
    },
    style_table={'overflowX': 'auto'},
    data=bardiya_sw.to_dict('records'),
   
    export_format="csv",
),
dcc.Interval(
        id='interval_component',
        interval=60000,
        n_intervals=0
    )
], className = 'eleven columns offset-by-one')


### Bardiya Deep deep well layout

bardiya_dtw_layout = html.Div([
    html.Div(
            [
                html.H1('GroundWater Monitoring', className = 'main_title'),
                html.Img(src = 'assets/images/partners.png', className = 'logos'),
                html.Img(src = 'assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gon.png', className = 'small_logos'),
                html.Img(src = 'assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Home', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
        ],className = 'nav_bar'),
    html.Div([
        dcc.Link('All Data', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),

         dcc.Link('Banke- Shallow Tube Well', href = '/pilot/bstw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Banke- Deep Tube Well', href = '/pilot/bdtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Shallow Tube Well', href = '/pilot/bastw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    dcc.Link('Bardiya- Deep Tube Well', href = '/pilot/badtw', style = {'font-family':'Times New Roman, Times', 'margin-left': '40px', 'font-size': '16px', 'text-decoration': 'none'}),
    ], style = {'background':'#fffccc'}),
    html.Br(),
    dash_table.DataTable(
    id='live_table_bardiya_dtw',
    columns=[{"name": i, "id": i} for i in bardiya_dw.columns],
    style_cell={
      
        'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
         
    },
    style_table={'overflowX': 'auto'},
    data=bardiya_dw.to_dict('records'),
   
    export_format="csv",
),
dcc.Interval(
        id='interval_component',
        interval=60000,
        n_intervals=0
    )
], className = 'eleven columns offset-by-one')

