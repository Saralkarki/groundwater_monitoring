import pandas as pd
import dash_leaflet as dl
import dash_leaflet.express as dlx
import os 



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

#extract lat lon from odk
lat = odk_latest.Geo_location.str.split(expand=True)[0]
lon = odk_latest.Geo_location.str.split(expand=True)[1]

#add back to measurement df with correct format
odk_latest['lat'] = lat.astype('float')
odk_latest['lon'] = lon.astype('float')



#load distric layers to add for context

file = './nepal-distr.geojson'

geo_df = gpd.read_file(file)


############### Then plot the figure

current_gw_level = go.Figure([
    go.Scattermapbox(
    mode = "text",
        showlegend = False, 
    lon = [-75, -80, -50], lat = [45, 20, -20],
    marker = {'size': 20, 'symbol': ["bus", "harbor", "airport"]},
    text = ["Bus", "Harbor", "airport"],textposition = "bottom right"),
    
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
    name="GW Level",
    lat=odk_latest['lat'],
    lon=odk_latest['lon'],
    mode='markers',
    marker=go.scattermapbox.Marker(
       size=14,
        color=odk_latest['gw_level'],
        colorscale='RdYlGn_r',
        showscale=True,
        ),
    )                            
])

current_gw_level.update_layout(
    hovermode='closest',
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
])
)

    