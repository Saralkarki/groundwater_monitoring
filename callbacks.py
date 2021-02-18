import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from options import all_options

import plotly.express as px
import plotly.graph_objects as go

from dash.exceptions import PreventUpdate

from layouts import info, get_info, get_info_home, info_home

from app import app

import dash_leaflet as dl
import dash_leaflet.express as dlx
import calendar
import pandas as pd

from options import tubewell_options, st_location_options, dt_location_options,swt_geojson,dwt_geojson,both_geojson,swt_geojson_bk,dwt_geojson_bk,both_geojson_bk,\
    swt_geojson_ba,dwt_geojson_ba,both_geojson_ba,modify_df,df_data , both_options, years, stw_district_wells, dtw_district_wells, all_wells

from data_import import download_data, map_data, save_file, parse_contents,\
     offline_data_transform, offline_df,cols_rename, transformed_data

import os



################# Home map ################################

### sidebar #####
# @app.callback(
#     Output('Tubewell_type_home','options'),
#     [Input('district','value')]
# )
# def display_district(seleted_district):
#     # print(seleted_district)
#     return [{'label': 'Deep Tube', 'value': 'dt'},{'label': 'Shallow Tube', 'value': 'st'} ]

## Well dynamic according to district and well type selected


@app.callback(
    Output('wells','options'),
    [Input('district','value'), Input('Tubewell_type_home','value')]
)
def display_wells(selected_district, well_type):
    if not selected_district:
        raise PreventUpdate
    if not well_type:
        raise PreventUpdate
    ## IF district Banke
        #And if ST show this
        #Or dt show this
    ## If Distirct Bardiya
        # IF st show this
        # If dt show this
        # or both
    ## if District both
        # ST
        # DT
        # Both
    if well_type == ['st']:
        district = selected_district[0]
        return [{'label': i, 'value': i} for i in stw_district_wells[district]]
    elif well_type == ['dt']:
        district = selected_district[0]
        return [{'label': i, 'value': i} for i in dtw_district_wells[district]]
    else:
        if selected_district == ['Banke']:
            return [{'label': i, 'value': i} for i in all_wells[selected_district[0]]]

        elif selected_district == ['Bardiya']:
            return [{'label': i, 'value': i} for i in all_wells[selected_district[0]]]
        else:
            return [{'label': i, 'value': i} for i in all_wells['all']]

        # district = selected_district
        


########################
@app.callback(
    Output('gw_map_home', 'children'),
    [Input('district','value'),Input('Tubewell_type_home', 'value'), Input('map_change','value')])
def display_value(district, tubewell_type,map_url):
    url = map_url
    if url == 'Overlay':
        image_url = "assets\\images\\banke_hydrogeo.png"
        image_bounds = [[24.05 ,  80.61], [28.773941, 84.12544]]
        url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

    else:
        image_url = ""
        image_bounds = [[23.05 ,  75.61], [29.773941, 83.12544]]
    
    attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>'
    # image_url = "groundwater_monitoring\assets\images\banke_hydrogeo.png"
    # image_bounds = [[28.05 ,  81.61], [29.773941, 83.12544]]
    if not district:
        x = dl.Map(dl.ImageOverlay( url=image_url, bounds=image_bounds),dl.TileLayer(url=url, attribution= attribution, style={'width': '100%', 'height': '500px'},center=[28.05,81.61] , zoom = 6))                 
        # raise PreventUpdate
    if not tubewell_type:
        x = dl.Map(dl.TileLayer(url=url, attribution= attribution, style={'width': '100%', 'height': '500px'},center=[28.05,81.61] , zoom = 6)) 
    
    elif len(tubewell_type) == 2:
        if district == ['Banke']:
            x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson_bk, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
        elif district == ['Bardiya']:
            x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson_ba, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
        else:
            x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),

    else:     
        value = tubewell_type[0]   
        if value == 'dt':
            if district == ['Banke']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson_bk, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            elif district == ['Bardiya']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson_ba, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            else:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),

        elif value == 'st':
            if district == ['Banke']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson_bk, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            elif district == ['Bardiya']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson_ba, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            else:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
        else:
            raise PreventUpdate
            
        
    return x
###### Input for the Kobo data coming in 
@app.callback( Output('timeseries_gw_data','figure'),
            [Input('gwt_home','click_feature'), Input('wells','value'), Input('data_logger_offline','value')])
def tubewell_no(map_click_feature, wells_dropdown_value, data_logger_value):
    if wells_dropdown_value is None:
        raise PreventUpdate
    if data_logger_value is None:
        raise PreventUpdate
    ### We have to merge the kobo database and the location data so that the kobo datafile has the column location based on well_no
    if len(wells_dropdown_value) > 0 or len(data_logger_value) > 0:
        # print(offline_df.columns)
        # for i in range(len(offline_df)):
        #     # print(offline_df[i],i)
        #     offline_data_transform(offline_df[i],cols_rename)   

        all_off_logger_df = pd.concat([all_offline_data[0],all_offline_data[1],all_offline_data[2],all_offline_data[3],
                            all_offline_data[4],all_offline_data[5],all_offline_data[6],all_offline_data[7],all_offline_data[8]])
        df = pd.read_csv('updated_data.csv')
        df['well_no'] = (df['sw_bk_well_no'].combine_first(df['bk_dw_no']).combine_first(df['well_no_sw_bardiya']).combine_first(df['well_no_dw_bardiya']))
        df_location_stw = pd.read_excel('data/preloaded_data/updated_well_data.xlsx')
        df_location_dtw = pd.read_excel('data/preloaded_data/updated_well_data.xlsx', sheet_name= "Deep tube wells")
        df_location =  pd.concat([df_location_stw, df_location_dtw])
        df_new = pd.merge(df, df_location, on='well_no', how = 'inner')      
        df_new.to_csv('offline_logger_data.csv')
        
        df_odk_data = pd.read_csv('offline_logger_data.csv')
        df_offline_logger = all_off_logger_df
        
        df_offline = df_offline_logger[df_offline_logger['Location'].isin(data_logger_value)]
        df_odk = df_odk_data[df_odk_data['Location'].isin(wells_dropdown_value)]
        df_odk['ODK'] = 'ODK'

        data = []  
        count = 0
        names = []
        for frame in [df_odk, df_offline]:
            if 'Water Level(meters)' in frame:
                frame.rename(columns = {'Water Level(meters)':'gw_level'}, inplace = True) 
            # data.append(frame['gw_level'])
            # print(len(data))
        #     df_odk = df_odk.sort_values(by=['today'])
        #     df_of = df_of.sort_values(by=['Date'])
            if 'ODK' in frame:
                frame = frame.sort_values(by=['today'])
                # print(frame)
                groups_odk = frame.groupby(by='Location')
                for group, df in groups_odk:
                    df["Month"] = pd.to_datetime(df.Month, format='%b', errors='coerce').dt.month
                    df = df.sort_values(by=['Month'])
                    df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
                    # print(df)
                    trace = go.Scatter(x=df['Month'].tolist(), 
                                    y=df['gw_level'].tolist(),
                                      name=f"{group}_odk")
                    data.append(trace)
            else:
                frame = frame.sort_values(by=['Month'])
                groups_offline = frame.groupby(by='Location')
                for group, df in groups_offline:
                    df["Month"] = pd.to_datetime(df.Month, format='%b', errors='coerce').dt.month
                    df = df.sort_values(by=['Month'])
                    df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])

                    # print(df)
                    trace_1 = go.Scatter(x=df['Month'].tolist(), 
                       y=df['gw_level'].tolist(),
                       name=group)
                    data.append(trace_1)

        layout =  go.Layout(xaxis={'title': 'Months'},
                    yaxis={'title': 'Groundwater in Meters(m)'},
                    hovermode='closest')
        figure = go.Figure(data=data, layout=layout)  
        figure.update_yaxes(autorange="reversed",range=(0, 10))
        
        
        return figure


    ## Now we have a new database to start graphinp with 
    ## Graph according to the values selected in the dropdown
    # if len(data_logger_value) > 0:
    #     # print(data_logger_value)
    #     df_offline = all_off_logger_df
    #     df_offline = df_offline[df_offline['Location'].isin(data_logger_value)]
        
    #     # print(df_offline)
    #     figure_offline = px.line(df_offline, x="Date", y="Water Level(meters)", color= 'Location')
    #     return figure_offline  
    #     # print(data_logger_value)
    # elif len(wells_dropdown_value) > 0:
    #     df = pd.read_csv('updated_data.csv')
    #     df['well_no'] = (df['sw_bk_well_no'].combine_first(df['bk_dw_no']).combine_first(df['well_no_sw_bardiya']).combine_first(df['well_no_dw_bardiya']))
    #     df_location_stw = pd.read_excel('data/preloaded_data/updated_well_data.xlsx')
    #     df_location_dtw = pd.read_excel('data/preloaded_data/updated_well_data.xlsx', sheet_name= "Deep tube wells")
    #     df_location =  pd.concat([df_location_stw, df_location_dtw])
    #     df_new = pd.merge(df, df_location, on='well_no', how = 'inner')      
    #     df_new.to_csv('test.csv')

    #     df = df_new[df_new['Location'].isin(wells_dropdown_value)]
    #     groups = df.groupby(by='Location')
    #     data = []
    #     colors=['red', 'blue', 'green']

    #     for group, df in groups:
    #         df = df.sort_values(by=['today'])
    #         trace = go.Scatter(x=df['Month'].tolist(), 
    #                    y=df['gw_level'].tolist(),
    #                    name=group)
    #         data.append(trace)
    #     layout =  go.Layout(xaxis={'title': 'Months'},
    #                 yaxis={'title': 'Groundwater in Meters(m)'},
    #                 hovermode='closest')
    #     figure = go.Figure(data=data, layout=layout)  
    #     figure.update_yaxes(autorange="reversed")
    #     return figure

    elif map_click_feature is not None:
        selected_tubewell_location = map_click_feature['properties']['well_no']
        data_map = map_data(selected_tubewell_location)       
        if not data_map.empty:
            fig = go.Figure(data=go.Scatter(x=data_map["Month"], y=data_map['gw_level']), 
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

## HOME MAP Hover feature 
@app.callback(
            Output("info_home","children"),
            [Input("gwt_home", "hover_feature")])
def state_hover_home(feature):
    return get_info_home(feature)


#### Historical data callaback########################

@app.callback(
    Output('wells_history','options'),
    [Input('district_history','value'), Input('Tubewell_type_history','value')]
)
def display_wells(selected_district, well_type):
    if not selected_district:
        raise PreventUpdate
    if not well_type:
        raise PreventUpdate
    if well_type == ['st']:
        district = selected_district[0]
        return [{'label': i, 'value': i} for i in stw_district_wells[district]]
    elif well_type == ['dt']:
        district = selected_district[0]
        return [{'label': i, 'value': i} for i in dtw_district_wells[district]]
    else:
        if selected_district == ['Banke']:
            return [{'label': i, 'value': i} for i in all_wells[selected_district[0]]]

        elif selected_district == ['Bardiya']:
            return [{'label': i, 'value': i} for i in all_wells[selected_district[0]]]
        else:
            return [{'label': i, 'value': i} for i in all_wells['all']]

        # district = selected_district
        
@app.callback(
    Output('gw_map', 'children'),
    [Input('district_history','value'),Input('Tubewell_type_history', 'value'), Input('map_change_history','value')])
def display_value(district, tubewell_type,map_url):
    url = map_url
    if url == 'Overlay':
        image_url = "assets\\images\\banke_hydrogeo.png"
        image_bounds = [[24.05 ,  80.61], [28.773941, 84.12544]]
        url = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'

    else:
        image_url = ""
        image_bounds = [[23.05 ,  75.61], [29.773941, 83.12544]]
    
    attribution = '&copy; <a href="https://stadiamaps.com/">Stadia Maps</a>'
    # image_url = "groundwater_monitoring\assets\images\banke_hydrogeo.png"
    # image_bounds = [[28.05 ,  81.61], [29.773941, 83.12544]]
    if not district:
        x = dl.Map(dl.ImageOverlay( url=image_url, bounds=image_bounds),dl.TileLayer(url=url, attribution= attribution, style={'width': '100%', 'height': '500px'},center=[28.05,81.61] , zoom = 6))                 
        # raise PreventUpdate
    if not tubewell_type:
        x = dl.Map(dl.TileLayer(url=url, attribution= attribution, style={'width': '100%', 'height': '500px'},center=[28.05,81.61] , zoom = 6)) 
    
    elif len(tubewell_type) == 2:
        if district == ['Banke']:
            x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson_bk, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
        elif district == ['Bardiya']:
            x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson_ba, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
        else:
            x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=both_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),

    else:     
        value = tubewell_type[0]   
        if value == 'dt':
            if district == ['Banke']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson_bk, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            elif district == ['Bardiya']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson_ba, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            else:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=dwt_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),

        elif value == 'st':
            if district == ['Banke']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson_bk, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            elif district == ['Bardiya']:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson_ba, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
            else:
                x = dl.Map(center=[28.05,81.61], zoom=8,
                children = [ 
                    dl.ImageOverlay(opacity=0.5, url=image_url, bounds=image_bounds),
                    dl.TileLayer(url=url, attribution= attribution), 
                    # dl.GeoJSON(data=bermuda),
                    dl.GeoJSON(data=swt_geojson, id = 'gwt_home',
                    hoverStyle=dict(weight=5, color='#333', dashArray='')), info_home]
                    ,style={'width': '100%', 'height': '500px'}, id = "map_x_home"),
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

#### upload data ########################
@app.callback(Output('output-data-upload', 'children'),
              Input('upload-data', 'contents'),
              State('upload-data', 'filename'),
              State('upload-data', 'last_modified'))
def update_output(list_of_contents, list_of_names, list_of_dates):
    if list_of_contents is not None:
        children = [
            parse_contents(c, n, d) for c, n, d in
            zip(list_of_contents, list_of_names, list_of_dates)]
        return children

   
