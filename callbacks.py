from dash.dependencies import Input, Output
from options import all_options

import plotly.express as px
import plotly.graph_objects as go

from dash.exceptions import PreventUpdate

from layouts import info, get_info, get_info_home, info_home

from app import app

import dash_leaflet as dl
import dash_leaflet.express as dlx

import pandas as pd

from options import tubewell_options, st_location_options, dt_location_options,swt_geojson,dwt_geojson,both_geojson,\
modify_df,df_data , both_options, years

from data_import import download_data, map_data




################# Home map ################################

@app.callback(
    Output('gw_map_home', 'children'),
    [Input('Tubewell_type_home', 'value')])
def display_value(value):
    if not value:
        x = dl.Map(dl.TileLayer(), style={'width': '100%', 'height': '500px'},center=[28.05,81.61] , zoom = 6)                 
        # raise PreventUpdate
    elif len(value) == 2:
        x = dl.Map(center=[28.05,81.61], zoom=10,
                children = [ 
                    dl.TileLayer(), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
    else:     
        value = value[0]   
        if value == 'dt':
            x = dl.Map(center=[28.05,81.61], zoom=10,
                children = [ 
                    dl.TileLayer(), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#666', dashArray='')),info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"), 
        elif value == 'st':
            x = dl.Map(center=[28.05,81.61], zoom=10,
                children = [ 
                    dl.TileLayer(), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#666', dashArray='')),info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"), 
        else:
            raise PreventUpdate
            
        
    return x
###### Input for the Kobo data coming in 
@app.callback(
    # [
        Output('timeseries_gw_data','figure'),
    # Output('timeseries_gw_data', 'children')],
    [
    # Input('Tubewell_location','value'),
    Input('gwt_home','click_feature')
    ])
def tubewell_no(map_click_feature):
    if map_click_feature is not None:
        selected_tubewell_location = map_click_feature['properties']['well_no']
        # print(selected_tubewell_location)
        data = map_data(selected_tubewell_location)       
        if not data.empty:
            fig = go.Figure(data=go.Scatter(x=data["Month"], y=data['gw_level']), 
            layout = go.Layout(margin = {'l':0, 't': 25, 'r' : 0, 'l' : 0}))
            fig.update_layout(title=f'Ground Water level of {selected_tubewell_location}',
                   xaxis_title='Months',
                   yaxis_title='Groundwater in mm'),
            fig.update_yaxes(autorange="reversed")
                
        else:
            fig = px.line(title = 'No Data Available')
        return fig
    else:
        fig = px.line()
        return fig

## HOME MAP Hover feature 
@app.callback(
            Output("info_home","children"),
            [Input("gwt_home", "hover_feature")])
def state_hover_home(feature):
    return get_info_home(feature)


#### Historical data callaback########################

@app.callback(
    Output('gw_map', 'children'),
    [Input('Tubewell_type', 'value')])
def display_value(value):
    if not value:
        x = dl.Map(dl.TileLayer(), style={'width': '100%', 'height': '500px'},center=[28.05,81.61] , zoom = 6)                 
        # raise PreventUpdate
    elif len(value) == 2:
        x = dl.Map(center=[28.05,81.61], zoom=10,
                children = [ 
                    dl.TileLayer(), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson, id = 'gwt',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x"),
    else:     
        value = value[0]   
        if value == 'dt':
            x = dl.Map(center=[28.05,81.61], zoom=10,
                children = [ 
                    dl.TileLayer(), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson, id = 'gwt',
                    hoverStyle=dict(weight=5, color='#666', dashArray='')),info]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x"), 
        elif value == 'st':
            x = dl.Map(center=[28.05,81.61], zoom=10,
                children = [ 
                    dl.TileLayer(), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson, id = 'gwt',
                    hoverStyle=dict(weight=5, color='#666', dashArray='')),info]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x"), 
        else:
            raise PreventUpdate
            
        
    return x
@app.callback(
    # [
        Output('timeseries_historical_data','figure'),
    # Output('timeseries_gw_data', 'children')],
    [
    # Input('Tubewell_location','value'),
    Input('gwt','click_feature'),
    Input('year-slider','value'),
    ])
def tubewell_location(map_click_feature, selected_year):
    if map_click_feature is not None:
        selected_tubewell_location = map_click_feature['properties']['well_no']
        data = modify_df(df_data, selected_tubewell_location, selected_year)
        # print(selected_year)
       
        # print(data)
        # data = df[df.year == selected_year]       
        if not data.empty:
            fig = go.Figure(data=go.Scatter(x=data["Months"], y=data['gw_level']), 
            layout = go.Layout(margin = {'l':0, 't': 25, 'r' : 0, 'l' : 0}))
            fig.update_layout(title=f'Ground Water level of {selected_tubewell_location}',
                   xaxis_title='Months',
                   yaxis_title='Groundwater in Meters(m)'),
            fig.update_yaxes(autorange="reversed")
                
        else:
            fig = px.line(title = 'No Data Available')
        return fig
    else:
        fig = px.line()
        return fig

## all_data map

@app.callback(Output('timeseries_historical_data_all','figure'),
    [Input('year-slider_all','value')])
def tubewell_location(selected_year):    
    data = df_data[df_data['year'].isin([selected_year])]
    # print(selected_year)
    data = data.loc[:,['Well number','location','month','value']]
    data.columns = ["Well Number","Location",'Months','gw_level']

    if not data.empty:
        fig = px.line(data, x="Months", y="gw_level", color='Well Number', hover_name="Location")
        
         
        # layout = go.Layout(margin = {'l':0, 't': 25, 'r' : 0, 'l' : 0}))
        fig.update_layout(title=f'Ground Water level(in Meters)',
                xaxis_title='Months',
                yaxis_title='Groundwater in Meters(m)'),
        fig.update_yaxes(autorange="reversed")
        return fig      
    else:
        fig = px.line(title = 'No Data Available')
    return fig
   
### PAST data map
@app.callback(Output("info","children"),
            [Input("gwt", "hover_feature")])
def state_hover(feature):
    return get_info(feature)



################# End historical data callback################



@app.callback(Output('live_table','data'),
            [Input('interval_component','n_intervals')])
def update_table(n):
    gw_sw = download_data()
    df = pd.read_csv("updated_data.csv")

    return df.to_dict('records')
