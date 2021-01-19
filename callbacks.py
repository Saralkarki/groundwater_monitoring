from dash.dependencies import Input, Output
from options import all_options

import plotly.express as px
import plotly.graph_objects as go

from dash.exceptions import PreventUpdate

from layouts import info, get_info

from app import app

import dash_leaflet as dl
import dash_leaflet.express as dlx

import pandas as pd

from options import tubewell_options, st_location_options, dt_location_options,swt_geojson,dwt_geojson,both_geojson,\
modify_df,df_2015_stw , both_options, years, df_2014_stw

from data_import import download_data, map_data


# Chained option for tubewell location
# @app.callback(
#     Output('Tubewell_location', 'options'),
#     [Input('Tubewell_type', 'value')])
# def set_tubewell_location(selected_tubewell_type):
#     if len(selected_tubewell_type) == 2:
#         x = both_options['both']
#         # print(option_selected)
#         option_selected = [{'label': i, 'value': i} for i in x]
#         # print(option_selected)
#     elif len(selected_tubewell_type) == 1:
#         x = selected_tubewell_type[0]
#         # print(x)
#         option_selected = [{'label': i, 'value': i} for i in all_options[x]]
    
#     else:
#         raise PreventUpdate
#         # option_selected = [{'label': 'None', 'value': 'None'}]
    # return option_selected

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
        Output('timeseries_gw_data','figure'),
    # Output('timeseries_gw_data', 'children')],
    [
    # Input('Tubewell_location','value'),
    Input('gwt','click_feature'),
    Input('year-slider','value'),
    ])
def tubewell_location(map_click_feature, selected_year):
    if map_click_feature is not None:
        selected_tubewell_location = map_click_feature['properties']['well_no']
        print(selected_tubewell_location)
        data = map_data(selected_tubewell_location)
        print(data)
        # if selected_year == 2015:
        #     data = modify_df(df_2015_stw,selected_tubewell_location) 
        #     # print(data)
        # elif selected_year == 2014:
        #     data = modify_df(df_2014_stw,selected_tubewell_location) 
        #     # print(data)
        # else:
        #     data = ()
        # print(selected_year)
        # print(data)
        # data = df[df.year == selected_year]
        
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
    # Code for Dropdown location selection

    # elif not selected_tubewell_location:
    #     fig = px.line()
    #     return fig
    # else:  
    #     data = modify_df(df_2015_stw,selected_tubewell_location) 
    #     if not data.empty:
    #         fig = go.Figure(data=go.Scatter(x=data["Months"], y=data['Measurement']))
    #         fig.update_layout(title=f'Ground Water level of {selected_tubewell_location}',
    #                xaxis_title='Months',
    #                yaxis_title='Groundwater in mm')
    #     else:
    #         fig = px.line(title = 'No Data Available')
    #     return fig
            
        # print(type(data))
        # px.scatter(data, x="Months", y="Measurement", title=f'Ground Water level of {selected_tubewell_location}',
        # mode='lines+markers')

#     # print(data)
#     # print(data)
#     # return data


# @app.callback(
#             Output("Test","children"),
#             [Input("gwt", "click_feature")])
# def state_click(feature):
#     if feature is not None:
#         return f"{feature['properties']['Location ']}, {feature['properties']['Well No.']}"

@app.callback(
            Output("info","children"),
            [Input("gwt", "hover_feature")])
def state_hover(feature):
    return get_info(feature)

        # return f"Location: {feature['properties']['Location ']}, Well No: {feature['properties']['Well No.']}"


@app.callback(Output('live_table','data'),
            [Input('interval_component','n_intervals')])
def update_table(n):
    gw_sw = download_data()
    df = pd.read_csv("updated_data.csv")

    return df.to_dict('records')
