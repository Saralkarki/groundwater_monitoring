import pandas as pd
import dash_leaflet as dl
import dash_leaflet.express as dlx
import os 
import plotly.graph_objects as go
import json
import geopandas as gpd


########################################### Current ODK - Measured GW Level #######################################################

################ First get the df and shapefiles

#mapbox token
token = 'pk.eyJ1IjoiYXVyZmVscyIsImEiOiJja25rZXNka2gwN3owMnNuMHl6MnRzNmUzIn0.tQH40pfi4OG7Q9_vVNtUVg'

#filter for only latest ODK observations
#first read, make date and sort by date
odk = pd.read_csv('updated_data.csv')
odk['today'] = pd.to_datetime(odk['today'])
odk = odk.sort_values('today',ascending=0)
#then drop all duplicates after first record
odk_latest = odk.drop_duplicates('well_no')
# print(odk_latest.shape)
# print(odk.shape)
#extract lat lon from odk
lat = odk_latest.Geo_location.str.split(expand=True)[0]
lon = odk_latest.Geo_location.str.split(expand=True)[1]
print(type(lat), type(lon))
lat = pd.to_numeric(lat, errors='coerce')
lon = pd.to_numeric(lon, errors='coerce')
# lat = lat.astype(str).astype(float)
# lon = lon.astype(str).astype(float)

#add back to measurement df with correct format
odk_latest['lat'] = lat
odk_latest['lon'] = lon
#load distric layers to add for context

file = './nepal-distr.geojson'

geo_df = gpd.read_file(file)

with open(file) as response:
    districts = json.load(response)


import numpy as np
odk_latest['hover1'] = np.repeat("GW Level: ", len(odk_latest))
odk_latest['hover2'] = odk_latest['gw_level'].astype(str)
odk_latest['hover3'] = odk_latest['today'].astype(str)
odk_latest['hover4'] = "mbgl"
odk_latest['hovtext'] = odk_latest['hover1'].str.cat(odk_latest['hover2'], sep = "<br>").str.cat(odk_latest['hover4'],sep = " ").str.cat(odk_latest['hover3'],sep = "<br>")

# print(odk['today'])

############### Then plot the figure

current_gw_level = go.Figure([
    
    go.Scattermapbox(
        lat= geo_df.centroid.y,
        lon= geo_df.centroid.x,
        mode='text',
        showlegend = False,
        marker=go.scattermapbox.Marker(
            size=14
        ),
        text= geo_df['DISTRICT'],
    ),    go.Scattermapbox(
    name="   Groundwater<br>   level<br>   in mbgl",
    lat=odk_latest['lat'],
    lon=odk_latest['lon'],
    mode='markers',
    text=odk_latest['well_no'],
    hoverinfo="text",
    hovertext=odk_latest['hovtext'],
    marker=go.scattermapbox.Marker(
       size=14,
        color=odk_latest['gw_level'],
        colorscale='RdYlGn_r',
       
        # showscale=True,
        # reversescale = True,
        colorbar={
        "tickmode":"array",
        "tickvals":[0,5,10,15],
        # "ticktext":["0","5","10","15"]
        }
        ),
    )                            
])


current_gw_level.update_layout(
    hovermode='closest',
	margin = dict(l = 0, r = 0, t = 50, b = 0,pad=0),
    mapbox=dict(
        accesstoken=token,
        bearing=0,
       center=go.layout.mapbox.Center(
            lat=28.2,
            lon=81.5
        ),
        pitch=0,
        zoom=8,
        layers =  [{
            'source': districts,
            'type': "line", 'below': "traces", 'color': "rgba(147,112,219)",
            "symbol":{"text":"HELLO","placement":"point"}},
]
       )
)

    