
import dash_core_components as dcc
import dash_table

import dash_html_components as html
import dash_leaflet as dl
import dash_leaflet.express as dlx
import dash_bootstrap_components as dbc
from figures import current_gw_level

from data_import import gw_df, banke_sw, banke_dw,bardiya_sw, bardiya_dw
import pandas as pd



from app import app

from options import tubewell_options, years_dict, both_options

# bermuda = dlx.dicts_to_geojson([dict(lat=32.299507, lon=-64.790337)])

def get_info(feature=None):
    header = [html.H4("Tubewell in Banke District")]
    if not feature:
        return header + ["Mouse over an area"]
    return header + [html.B(f"Location: {feature['properties']['Location']}"), html.Br(),
    html.B(f"Well No: {feature['properties']['well_no']}")]

def get_info_home(feature=None):
    header = [html.H4("Tubewells in Banke District")]
    if not feature:
        return header + ["Hover mouse over an area and click"]
    return header + [html.B(f"Location: {feature['properties']['Location']}"), html.Br(),
    html.B(f"Well No: {feature['properties']['well_no']}")]

# Create info control.
info = html.Div(children=get_info(), id="info", className="info",style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "1000"})
info_home = html.Div(children=get_info_home(), id="info_home", className="info",style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "912"})
map_buttons = html.Div(children=get_info(), id="info", className="info",style={"position": "absolute", "top": "10px", "right": "10px", "z-index": "1000"})
app.title = 'Digital Groundwater Monitoring Dashboard'



### Realt time moniroting layouts 


sidebar =      html.Div([
                html.H5("Districts"),
                dcc.Checklist(id='district',options=[{'label': ' Banke', 'value': 'Banke'},{'label': ' Bardiya ', 'value': ' Bardiya '}],value=['Banke'], labelStyle={'display': 'inline-block'}),
                html.H5('Type of well'),
                dcc.Checklist(id = 'Tubewell_type_home', options = tubewell_options, value = ['st'], labelStyle={'display': 'inline-block'}),
               
                    html.Br(),
            html.H5("Manually measured wells"),
          html.Div([
            dcc.Dropdown(
                id='wells',
                value=['Rohini Khola'],
                multi=True
            ),]),
            html.Br(),
            html.H5("Offline Data logger"),
            dcc.Dropdown(
                id='data_logger_offline',
                #'Rohini Khola','Banjare Gau', 'Channawa','D-Gau','Jaispur','Kalhanshangau','Khadaicha','Piprahawa','Shikanpurwa'
                options=[
        {'label': 'Channawa', 'value': 'Channawa'},
        {'label': 'Piprahawa', 'value': 'Piprahawa'},
        {'label': 'Shikanpurwa', 'value': 'Shikanpurwa'},
         {'label': 'Khadaicha', 'value': 'Khadaicha'},
        {'label': 'D-gaon', 'value': 'D-Gau'},
        {'label': 'Kalhanshangau', 'value': 'Kalhanshangau'},
        {'label': 'Banjare Gau', 'value': 'Banjare Gau'},
          {'label': 'Jaispur', 'value': 'Jaispur'},
          {'label': 'Rohini Khola', 'value': 'Rohini Khola'}],
                value=['Rohini Khola','Channawa','Piprahawa','Jaispur','Banjare Gau','Kalhanshangau','D-Gau','Khadaicha','Shikanpurwa'],
                multi=True
            ),


            ])


sidebar_card = dbc.Card([
    dbc.CardHeader("Select wells to display:"),
    dbc.CardBody(sidebar)
    ],)


gw_rt_map =         html.Div([
            



            html.Br(),
            html.Div([
                html.Div([
                   dcc.RadioItems(id = 'map_change',
                    options=[
                    {'label': 'Default', 'value': 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'},
                    {'label': 'Stadia', 'value': 'https://tiles.stadiamaps.com/tiles/alidade_smooth_dark/{z}/{x}/{y}{r}.png'},
                    {'label': 'Topo', 'value': 'https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png'},                
                    {'label': 'Overlay', 'value': 'Overlay'}],
                value='https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',labelStyle={'display': 'inline-block'})  
                ]),
                html.Br(),
                html.Div(id = 'gw_map_home'),
                dl.Map(center=[28.05,81.61], zoom=18, children=[dl.TileLayer(), dl.GeoJSON(id = "gwt_home"), info_home]),
             
            ], className = 'twelve columns'),



            #main window
 
# Main div      
        ], className = 'twelve columns')
# Main container      

gw_odk_levels =             html.Div([
      #          html.Div([html.H6("GroundWater Level")], className = 'graph_text'),
                dcc.Graph(id = 'timeseries_gw_data',
                    style={'width': '200%', 'height': '500px', 'margin-top': "-15px"}),
                # html.Div([ dcc.Slider(id='year-slider',value = 2015, min = 1996, max = 2015,marks=years_dict,step=None)], style = {'display':'none'}),
               
                #  dcc.Graph(id = 'test_1'),

            ],className = 'six columns main_window ')   


offline_levels =   html.Div([

       #         html.H1("Ground Water Measurement (Offline Data logger)"),
                # html.H6("Click on the Well number on the legend to select and deselect the wells"),
                
                dcc.Graph(id = 'offline_data_logger_graph',style={'width': '95%', 'height': '600px', 'margin-top': "-15px"}),
                # dcc.Slider(id='year-slider_all',value = 2015, min = 2001, max = 2015,marks=years_dict,step=None)
            ],className = 'row twelve columns offset-by-one column', style = {'margin-top':'30px'}),

odkrt_levels =   html.Div([

       #         html.H1("Ground Water Measurement (Offline Data logger)"),
                # html.H6("Click on the Well number on the legend to select and deselect the wells"),
                
                dcc.Graph(figure = current_gw_level,style={'width': '200%', 'height': '600px', 'margin-left':"-15px",'margin-right':"20px", 'margin-top': "-15px"}),
                html.P("Data for wells recorded during different times of month. Please hover on the wells to get precise readings of the wells")
                # dcc.Slider(id='year-slider_all',value = 2015, min = 2001, max = 2015,marks=years_dict,step=None)
            ],className = 'row twelve columns offset-by-one column', style = {'margin-top':'5px'}),



rtmap_card = dbc.Card([
    dbc.CardHeader("Locations of monitoring wells:"),
    dbc.CardBody(gw_rt_map)
    ],)

rtodk_card = dbc.Card([
    dbc.CardHeader("ODK based groundwater measurements:"),
    dbc.CardBody(gw_odk_levels)
    ],)

offline_card = dbc.Card([
    dbc.CardHeader("Offline logger based groundwater measurements:"),
    dbc.CardBody(offline_levels)
    ],)

current_card = dbc.Card([
    dbc.CardHeader("Last recorded ODK measurement of groundwater Level:"),
    dbc.CardBody(odkrt_levels)
    ],)




side = html.Div([
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    dbc.Row([
        dbc.Col([html.Div(sidebar_card,className="sticky-top",style={"top":100})],width={"offset":2,"size":2}),
        dbc.Col([html.Div(rtmap_card),
            dbc.Row(html.Br()),
            dbc.Row(html.Br()),
            dbc.Row([dbc.Col([html.Div(current_card)])]),
            dbc.Row(html.Br()),
            dbc.Row(html.Br()),
            dbc.Row([dbc.Col([html.Div(rtodk_card)])]),
            dbc.Row(html.Br()),
            dbc.Row(html.Br()),
            dbc.Row([dbc.Col([html.Div(offline_card)])])],width=6),

            
        ],),

    ])


main_layout = html.Div(
    [

        side,
       

    ], className = 'twelve columns')






################
####################Historical data######################









hist_sidebar = html.Div([
                html.H5("Districts"),
                dcc.Checklist(id='district_history',options=[{'label': 'Banke', 'value': 'Banke'},{'label': 'Bardiya', 'value': 'Bardiya'}],value=['Banke'], labelStyle={'display': 'inline-block'}),
                html.H5('Type of well'),
                dcc.Checklist(id = 'Tubewell_type_history', options = tubewell_options, value = ['st']),
               
                  html.Div([
            dcc.Dropdown(
                id='wells_history',
                value= 'bk-sw-01',
                multi=False
            ),],style={'width': '100%', 'float': 'left','display': 'inline-block'}),
            html.Br(),
            # html.H5("Offline Data logger"),
        #     dcc.Dropdown(
        #         id='data_logger_offline_history',
        #         #'Rohini Khola','Banjare Gau', 'Channawa','D-Gau','Jaispur','Kalhanshangau','Khadaicha','Piprahawa','Shikanpurwa'
        #         options=[
        # {'label': 'Channawa', 'value': 'Channawa'},
        # {'label': 'Piprahawa', 'value': 'Piprahawa'},
        # {'label': 'Shikanpurwa', 'value': 'Shikanpurwa'},
        #  {'label': 'Khadaicha', 'value': 'Khadaicha'},
        # {'label': 'D-gaon', 'value': 'D-Gau'},
        # {'label': 'Kalhanshangau', 'value': 'Kalhanshangau'},
        # {'label': 'Banjare Gau', 'value': 'Banjare Gau'},
        #   {'label': 'Jaispur', 'value': 'Jaispur'},
        #   {'label': 'Rohini Khola', 'value': 'Rohini Khola'}],
        #         value=['Rohini Khola'],
        #         multi=True
        #     ),


            ], ),
            


single_hist_graph = html.Div([
                html.Div([html.H6("Ground water level")], className = 'graph_text'),
                dcc.Graph(id = 'timeseries_historical_data',style={'width': '100%', 'height': '600px', 'margin-top': "-15px"}),
                # html.Div([ dcc.Slider(id='year-slider',value = 2015, min = 2001, max = 2015,marks=years_dict,step=None)]),
               
                #  dcc.Graph(id = 'test_1'),

            ],),
           

all_hist_graph = html.Div([
                html.H6("Click on the well number on the legend to select and deselect the wells"),
                html.Br(),
                dcc.Graph(id = 'timeseries_historical_data_all',style={'width': '100%', 'height': '500px', 'margin-top': "-5px"}),
         #       dcc.Slider(id='year-slider_all',value = 2015, min = 2001, max = 2015,marks=years_dict,step=None)
            ],)



#card for formatting sidebar on historical 
hist_sidebar_card = dbc.Card([
    dbc.CardHeader("Select wells to display:"),
    dbc.CardBody(hist_sidebar)
    ],)


single_historical_graph_card = dbc.Card([
    dbc.CardHeader("Single well historical water level:"),
    dbc.CardBody(single_hist_graph)
    ],)

all_hist_graph_card = dbc.Card([
    dbc.CardHeader("All wells historical water level:"),
    dbc.CardBody(all_hist_graph)
    ],)




#this is the strucutre of the page
hist_side = html.Div([
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    dbc.Row(html.Br()),
    dbc.Row([
        dbc.Col([html.Div(hist_sidebar_card,className="sticky-top",style={"top":100})],width={"offset":2,"size":2}),
        dbc.Col([html.Div(single_historical_graph_card),
            dbc.Row(html.Br()),
            dbc.Row(html.Br()),
            dbc.Row([dbc.Col([html.Div(all_hist_graph_card)])])],width=6),

            
        ],),

    ])

#this read the structure of the page - keep it small for easy exchange
history_layout = html.Div(
    [
        hist_side,
    ], className = 'twelve columns')










###########################################  Dataset download page

#always create the div for the data table and download
# then add it into a bootstrap card for layout 


#functions

def showTable(table):
    return html.Div([

    html.Br(),
    dash_table.DataTable(
    id='live_table',
    columns=[{"name": i, "id": i} for i in table.columns],
     style_cell={
      
        'height': 'auto',
        # all three widths are needed
        'minWidth': '180px', 'width': '180px', 'maxWidth': '180px',
        'whiteSpace': 'normal'
         
    },
    style_table={'overflowX': 'auto','height': '500px', 'overflowY': 'auto'},
    data=table.to_dict('records'),
   
    export_format="csv",
),

#removed because refresshing messes with the row selection
#  should update on page load
# But not tested ,keeping this for future need
#dcc.Interval(
#        id='interval_component',
#        interval=60000,
#        n_intervals=0
#    )
], className = 'eleven columns offset-by-one')

def tableCard(table):
    return html.Div([
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardBody([table])
                ])
            ],width={"offset":2,"size":8})
        ])
    ])

# for all tubewells
aTW = showTable(gw_df)
pilot_layout = tableCard(aTW)


# banke shallow tubewell data download
bSTW = showTable(banke_sw)
banke_stw_layout = tableCard(bSTW)


### Banke Deep deep well layout
bDTW = showTable(banke_dw)
banke_dtw_layout = tableCard(bDTW)

### Bardiya Shallow well layout
baSTW = showTable(bardiya_sw)
bardiya_stw_layout = tableCard(baSTW)

### Bardiya Deep deep well layout
baDTW = showTable(bardiya_dw)
bardiya_dtw_layout = tableCard(baDTW)

### meta data layout


meta_layout = html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
 
    html.Div([dcc.Markdown('''

## Background on groundwater monitoring in Nepal
Nepal's Terai has an estimated 8,800 MCM of groundwater reserves, based on assessments carried out in the 1970s and 1980s, and abstraction of groundwater from these aquifers has steadily increased with irrigation being the main water user. Electrification, promotion of solar pumps, increasing private investments in diesel pump irrigation and growing industrial water use are progressively increasing the demand for groundwater in Nepal's Terai and localized reports of groundwater depletion have started to surface.
Monitoring the water levels of the Terai's aquifers is thus critical to ensure that groundwater development does not deplete the resource beyond sustainable limits. While the responsibilities of groundwater management are currently spread across different governmental bodies, the GWRDB retains a mandate for groundwater monitoring activities that are to be implemented through its branch offices.  


Specifically, Nepal's GWRDB has the following main objectives:

> > 1. Identification of groundwater potential area in the Terai (shallow and deep aquifer) through geophysical survey and investigation tubewells.
2. Exploitation of shallow and deep aquifer in the Terai for irrigation and drinking purpose.
3. Develop technical manpower related to groundwater field.
4. Regular monitoring of existing investigation tubewells for water level fluctuation, groundwater reserves and water quality.
5. Study and investigation of mountain and Karst aquifer.
6. Groundwater Resources Development Board (GWRDB), located at Babarmahal, Kathmandu is responsible to carry out above mentioned activities through its 8 branch offices. 


Groundwater Field Offices are located at Biratnagar, Lahan, Mahottari, Birganj, Butwal, Dang, Nepalganj and Dhangadhi.
As of now, each of the branch offices employs one data collector per overseen district who measures the groundwater level of ca. 20 wells per district on a monthly basis. These measurements are then transcribed from pen and paper into an excel worksheet that is stored with the GWRDB.


The current procedure has three major shortcomings: 

> > 1. The process introduces a time lag for data availability and potential errors in transcribing the data. 
2.  The data is not easily accessible to a wider audience of interested users, limiting the use of these data for research and development planning.
3. The data is not easily visualizes for mapping of groundwater levels in space and time and for processing into information for different use cases.

## Objective of this Dashboard

The goal of this project activity is to pilot an open data system for groundwater data in Banke district with the aim to develop a system that can be scaled to other districts of Nepal.
The sub-objectives include: 
> > 1. Evaluate the efficacy of different approaches for automatizing data groundwater measurements and data collection (Manual, ODK-based, offline loggers, online loggers).
2. Develop a dashboard that displays the groundwater monitoring data catering to different use cases. 
3. Provide access to  groundwater level data and important auxiliary information for users of the dashboard.

## Dashboard development and data collection

The dashboard is being developed on a continuous basis. This first version is aimed to provide rapid support and real-time visualization for the ongoing data collection efforts. In the background we are constantly developing the feature set of the dashboard based on experience and user feedback. We therefore kindly invite anybody to get in touch with us and provide any feedback or demands for additional features. 
The dashboard is divided into three different components: 
> > 1. The real-time monitoring data
2. A spreadsheet with more information about each measurement and the possibility for downloading the data.
2. An overview of the historical data for Banke district.

### Digital monitoring

This section displays in real-time the data that is being collected for this specific project during the year 2021. To evaluate different data collection approaches, this section categorizes data points into three different categories:
> > 1. ODK-based data collection.
	- This method replaces the manual data entry with ODK-supported data entry on a tablet. After measuring the water level, the data collector immediately enters the data in a survey form on his tablet which is immediately send to the cloud and processed. Data collection takes place on a monthly basis.
2. Offline data loggers.
	- This method uses 10 low-cost offline data loggers to record daily water levels. The data loggers need to be read out and uploaded to the data base manually, which takes place on a 2-weekly basis.
3. Online data loggers (in operatio with delay and currently integrated into the dashboard)
	- Online data loggers transmit information to the cloud in real-time by using the cellular network. Powered through a small solar panel, the system ready the water level and immediately transmits the information to the online survey from where it is further processed and visualized.

### Download monitoring data
This section shows the uploaded data. It includes all the variables that are submitted to the server including location, well number, name of data collector, date, measurement details and the final groundwater level for the ODK based data, and groundwater level for the offline loggers. By clicking the "export" button the whole dataset can be downloaded. Note, that this dataset has not been screened for errors so use with caution. 
### Historical data
These data have been manually collected and curated since the year 2000. However, some years and data points are missing and typos have not been fixed yet. You can click both on the wells in the map or on the graph in the bottom to select and de-select wells of interest. Below the graphs you can select the year of interest.
### Well selection
The GWRDB oversees ~20 shallow and ~5 deep tubewells for monitoring purposes per district. This pilot did not establish additional wells but uses the existing ones. The offline wells were selected in order to capture the North-South and East-West gradient. However, some wells were not practical to install and had to be exchanged for more feasible alternatives.
### Geographical setting and hydro-geological Characteristics
Nepal's Terai belongs to the Northernmost section of the Indo-Gangetic Plains that stretch from the foothills of the Himalayas to the Ganges Rivers in the South at around 100 masl. The aquifers thus belong to the Indo-Gangetic Basin alluvial aquifer. General characteristics of the aquifers can, for example, be found in Bonsor et al. (2017) https://doi.org/10.1007/s10040-017-1550-z. A typical cross section of the Terai aquifer looks like the following (with yellow being coarser sand layers of good aquifer material, Bonsor et al. 2017):'''),
html.Br(),
html.Br(),
html.Br(),
html.Img(src = 'assets/images/terai_aquifer.webp'),
html.Br(),
html.Br(),

# ![Terai Aquifer Schematic](/groundwater_monitoring/assets/metadata_page/terai_aquifer.webp) 

dcc.Markdown('''
Nepal's Terai aquifers are comprised of alluvial and poorly sorted aquifer material. Several layers of aquifer material are intersected by several layers semi-confining clay layers. Water levels for aquifers range from 0 to 10 mbgl with an average of 4.5 mbgl. The following map has been produced by the GWRDB based on the water level measurements of the GWRDB/UNDP tubewells of 1993:
'''),

html.A(html.Img(src = 'assets/images/banke_hydrogeo.png', style = {'width': '100%'}), href = "assets/images/banke_hydrogeo.png"),
# ![Aquifer Characteristics Map Banke](/groundwater_monitoring/assets/metadata_page/) 
html.H5("click on the image to see full-view"),
html.Br(),

dcc.Markdown(''' '''),
## Contact

    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),

    ], className= 'container'),
    



], className = 'eleven columns offset-by-one')
############################

upload_layout = html.Div(
    [
# header div
        html.Div(
            [
                html.H1('Real-time monitoring database', className = 'main_title'),
                html.Img(src = '/assets/images/partners.png', className = 'logos'),
                html.Img(src = '/assets/images/csisa-logo.png', className = 'small_logos'),
                html.Img(src = '/assets/images/gon.png', className = 'small_logos'),
                html.Img(src = '/assets/images/gwrdb-new.gif', className = 'gwrdb_logo'),
                # html.Img(src = 'assets/images/csisa-logo.png', className = 'logo_csisa'),
                html.Br(),
                
                # html.Img(src = 'assets/images/ccafs-logo.png', className = 'logo'),
            ], className = 'header'
        ),
        ### Navigation bar
        html.Div([
            
            dcc.Link('Real-Time Monitoring', href = '/realtime', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Database', href = '/pilot', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Past-Database', href = '/historical_data', style = {'font-family':'Times New Roman, Times', 'margin-right': '50px', 'font-size': '18px', 'text-decoration': 'none'}),
            dcc.Link('Meta-Data', href = '/', style = {'font-family':'Times New Roman, Times', 'margin-right': '40px', 'font-size': '18px', 'text-decoration': 'none'}),


        ],className = 'nav_bar'),
#main body
        html.Div([
            html.H1("Upload"),
            html.H6("Upload Offline logger Data file "),
            dcc.Upload(
        id='upload-data',
        children=html.Div([
            'Drag and Drop or ',
            html.A('Select Files')
        ]),
        style={
            'width': '100%',
            'height': '60px',
            'lineHeight': '60px',
            'borderWidth': '1px',
            'borderStyle': 'dashed',
            'borderRadius': '5px',
            'textAlign': 'center',
            'margin': '10px'
        },
        # Allow multiple files to be uploaded
        multiple=True
    ),
    html.Div(id='output-data-upload'),
    html.Div([
        dcc.Markdown(''' 
         ### Upload Instructions:
         1. Click on the Drag and Drop or Select Files area
         2. Upload the CSV file using the dialog box
         3. ** The Upload file needs to be a .CSV file **
         4. ** Please use the CSV file received from the HOBO APP ** (Refer to the manual for column the sample view)
         5. Refer to the manaul for approriate filenames

        
        '''),

    ], className = 'offset-by-one column')
]),
        
# Main container      
    ], className = 'twelve columns offset-by-one column'
)







### Home layout


home_layout = html.Div([
    html.Br(),
    html.Br(),
    html.Br(),
    html.Br(),
 
    html.Div([dcc.Markdown('''
# Introduction and user instructions

This website is a product of the CSISA-Resilience project in partnership with Nepal’s Groundwater Resources Development Board and aims to contribute to Nepal’s capacity to build a digital groundwater monitoring system through a small pilot project in the USAID Feed the Future Zone of Nepal’s Tarai region. The ongoing expansion of groundwater resources development will undoubtedly provide great contribution to Nepal’s irrigation sector and food security. Along this way, a digital groundwater monitoring system will be critical to help the country guide the development and management of the resource by providing decision-makers and communities with adequate spatial evidence and information about the opportunities and risks for sustainable and equitable groundwater use.

The Cereal Systems Initiative in South Asia (CSISA; www.csisa.org) is supported by USIAD and the Bill and Melinda Gates Foundation and is led by the International Maize and Wheat Improvement Center (CIMMYT) and implemented jointly with the International Water Management Institute (IWMI), International Food Policy Research Institute (IFPRI) and the International Rice Research Institute (IRRI). In Nepal, new support from USAID has led to the implementation of the CSISA Covid-19 Response and Resilience Activity (CSISA-Resilience), which is also implemented with Texas A&M University, Cornell University, and International Development Enterprises (iDE). CSISA-Resilience involves two inter-linked objectives that address CSISA’s strengths in core areas needed to assist in COVID-19 response and recovery, as well as Nepal’s longer-term building of processes and structures that can enhance resilience to shocks, with emphasis empowering youth and overcoming challenges faced by women headed farm households. The views expressed on this website do not necessarily reflect the views of the donors.

## Contact

In case you should have any question or feedback kindly get in touch and contact Anton Urfels, who leads this activity, at a.urfels@cgiar.org. 

## How to use this website?
- This is the beta version of the dashboard and is designed to provide rapid access to the data that we are collecting and for soliciting rapid feedback about the data collection and visualization. We aim to upgrade this dashboard in the near future with a richer feature set.
- You are currently on the [home page](/home). Here we provide a brief overview of this project activity and instruction on how to use this dashboard.  
- The [Meta-data page](/) provides more detailed background information and other relevant meta-data
- The [Digtial groundwater monitoring page](/realtime) provides and overview of recently collected data through different monitoring methods (see below for more information). You can toggle the map to display different monitoring methods and click on the wells to see the data collected for each specific location and methods.
- The [Download monitoring data page](/pilot) provides access to the detailed data that has been collected and you can download it in CSV format. In the navigation bar you can also select the district and well type to show data for. 
- The [Historical data page](/historical_data) contains data that has been collected by the GWRDB since the year 2000. Note that this data has not been cleaned, but it can be used to obtain a better feel for the groundwater level fluctuations that are typical in the region.

'''),

    html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),
html.Br(),

## Contact

    ], className= 'container'),
    



], className = 'eleven columns offset-by-one')
############################
