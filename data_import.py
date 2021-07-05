import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import time, sched

import dash_html_components as html
import dash_core_components as dcc

import calendar
from urllib.parse import quote as urlquote

url= "https://kc.humanitarianresponse.info/api/v1/data/669773.json"
auth = HTTPBasicAuth('gw_monitoring', 'gwmonitor@2020')

import base64
import io
import datetime
import dash_table
import os
from os import path



# files = {'filename': open('filename.txt','rb')}
def download_data():
    download = requests.get(url, auth=auth )
    # col_names = ['Enumerator Name','Geo_location','Municipality','village_name','ward','well_type','well_no_stw','well_no_dtw','gw_level','Height_of_measurement','measurement_unit',"Notes"]
    # df = pd.read_csv('updated_data.csv')  
    j = requests.get(url, auth=auth )
    df_json = j.json()
    gw_df = pd.DataFrame.from_dict(df_json)
#     print(gw_df.columns)
#     print(len(gw_df.columns))  
    # 'sw_bk_well_no','bk_dw_no','well_no_sw_bardiya','well_no_dw_bardiya',
    if not 'Main_group/location_details/sw_bk_well_no' in gw_df.columns:
        #     print("NO cols_1")
            gw_df['sw_bk_well_no'] = '' 
    if not 'Main_group/location_details/bk_dw_no' in gw_df.columns:
        #     print("NO cols_2")
            gw_df['bk_dw_no'] = '' 
    
    if not 'Main_group/location_details/well_no_sw_bardiya' in gw_df.columns:
        #     print("NO cols_3")
            gw_df['well_no_sw_bardiya'] = '' 
    
    if not 'Main_group/location_details/well_no_dw_bardiya' in gw_df.columns:
            gw_df['well_no_dw_bardiya'] = '' 
        #     print("NO cols_4")
#     print(len(gw_df.columns))   
#     print(gw_df.columns)       
    # gw_df = pd.read_json(download.text)   
    if len(gw_df.columns) != 36:
        #     return html.Div([html.H1("ERROR: With fetching the data. Please check later")])
            df = pd.DataFrame()
        #     df = pd.read_csv('updated_data.csv')  
            print("ERROR")
    else:
        gw_df.columns = ['_id', 'formhub/uuid', 'start', 'end', 'today', 'deviceid',
       'Enumerator Name',
       'District',
       'geo_location',
       'well_type',
       'sw_bk_well_no',
       'measurement_point_cm',
       'Well_photo_Use_the_ed_measurement_point',
       'Measurement_of_tape_ent_point_MP_in_m',
       'wet_point_measruement_on_tape',
       'gw_level_from_mp',
       'mp_in_m', 'gw_level',
       '__version__', '_version_', 'meta/instanceID', '_xform_id_string',
       '_uuid', '_attachments', '_status', 'Geo_location', '_submission_time',
       '_tags', '_notes', '_validation_status', '_submitted_by',
       'bk_dw_no',
       'well_no_sw_bardiya',
       'well_no_dw_bardiya',
       'Audio_Notes',
       'Notes']
    ### How did the columns change??
    #     gw_df.columns = ['_notes',
    #    'Measurement_of_tape_ent_point_MP_in_m', '_tags',
    #    '_xform_id_string', 'meta/instanceID',
    #    'gw_level_from_mp', 'end',
    #    'gw_level',
    #    'Well_photo_Use_the_ed_measurement_point',
    #    'mp_in_m', 'start', '_attachments', '_version_',
    #    '_status', '__version__', 'today',
    #    'sw_bk_well_no',
    #    'Enumerator Name',
    #    'Geo_location', '_validation_status',
    #    '_uuid', 'well_type', 'formhub/uuid',
    #    'District', '_submission_time',
    #    '_geolocation', '_submitted_by',
    #    'wet_point_measruement_on_tape', 'deviceid',
    #    'measurement_point_cm', '_id',
    #    'Notes',
    #    'Audio_Notes',
    #    'well_no_sw_bardiya', 'bk_dw_no',
    #    'well_no_dw_bardiya']
        all_cols = ['Enumerator Name','Geo_location','District',
        'well_type','sw_bk_well_no','bk_dw_no','well_no_sw_bardiya','well_no_dw_bardiya','measurement_point_cm',
        'Measurement_of_tape_ent_point_MP_in_m', 'wet_point_measruement_on_tape','gw_level',
        'Notes','today','Audio_Notes']

        # print(gw_df)
        df = pd.DataFrame()
        
        for cols in all_cols:
                df[cols] = gw_df[cols]
        # df = gw_df.copy()  
        # print(df) 
        # df = df.sort_values(by='today')
        # print(df)
        # df['Enumerator']
            # print(gw_df[i])   
        df['well_no'] = (df['sw_bk_well_no'].combine_first(df['bk_dw_no']).combine_first(df['well_no_sw_bardiya']).combine_first(df['well_no_dw_bardiya']))
        ## onvertt he today data to date    
        df['today'] = pd.to_datetime(df['today'])
        df['Month'] = df['today'].dt.month
        # print(df['Month'])
        df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])   
        df.to_csv('updated_data.csv')
    return df 

gw_df = download_data()


### Data to map the values
def map_data(well_number):
        df = pd.read_csv('updated_data.csv')
        cols = ['well_no','Month','gw_level']
        df = df[cols]
        x = df[df['well_no'].isin([well_number])]
        # print(x)
        return x


#banke SW data


banke_sw = gw_df[(gw_df['District']=="Banke") & (gw_df['well_type'] == 'sw')]
banke_sw = banke_sw[['Enumerator Name','Geo_location','District',
        'well_type','sw_bk_well_no','gw_level',
        'measurement_point_cm',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]




banke_dw = gw_df[(gw_df['District']=="Banke") & (gw_df['well_type'] == 'dt')]
banke_dw = banke_dw[['Enumerator Name','Geo_location','District',
        'well_type','bk_dw_no','gw_level',
        'measurement_point_cm',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]



bardiya_sw = gw_df[(gw_df['District']=="Bardiya") & (gw_df['well_type'] == 'sw')]


bardiya_sw = bardiya_sw[['Enumerator Name','Geo_location','District','well_type','well_no_sw_bardiya','gw_level',
        'measurement_point_cm','Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]

    


bardiya_dw = gw_df[(gw_df['District']=="Bardiya") & (gw_df['well_type'] == 'dt')]
bardiya_dw = bardiya_dw[['Enumerator Name','Geo_location','District',
        'well_type','well_no_dw_bardiya','gw_level',
        'measurement_point_cm',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]



# print(gw_df)
print("JOB DONE")
# UPLOAD_DIRECTORY = "data/uploaded_data"

# if not os.path.exists(UPLOAD_DIRECTORY):
#     os.makedirs(UPLOAD_DIRECTORY)

def save_file(name, content):
        """Decode and store a file uploaded with Plotly Dash."""
       
        try:
                if 'csv' in name:
                        data = content.encode("utf8").split(b";base64,")[1]
                        with open(os.path.join(UPLOAD_DIRECTORY, name), "wb") as fp:
                                fp.write(base64.decodebytes(data))

                        df = pd.read_csv(name, skiprows=[1])
                        return html.Div(['There was an error processing this file.'])
                        # print(df)
        except Exception as e:
                print(e)
                return html.Div(['There was an error processing this file.'])

def parse_contents(contents, filename, date):
    content_type, content_string = contents.split(',')
    data = contents.encode("utf8").split(b";base64,")[1]    
    decoded = base64.b64decode(content_string)
    try:
        
        if 'csv' in filename:
            if path.exists(filename):
            # Assume that the user uploaded a CSV file
                df = pd.read_csv(io.StringIO(decoded.decode('utf-8')), skiprows=[0])
                # df.insert(loc=0, column='', value='')
                df.to_csv(filename, mode='a', header=False)
            # with open(os.path.join(UPLOAD_DIRECTORY, filename), "wb") as fp:
            #         fp.write(base64.decodebytes(data))
        else:
                return html.Div(['There was an error processing this file. Please check if it is a CSV file'])
    except Exception as e:
        print(e)

    return html.Div([
        html.H5(f"{filename} has been uploaded"),
        html.H6(datetime.datetime.fromtimestamp(date)),

        dash_table.DataTable(
            data=df.to_dict('records'),
            columns=[{'name': i, 'id': i} for i in df.columns]
        ),

        html.Hr(),  # horizontal line

        # For debugging, display the raw contents provided by the web browser
        html.Div('Raw Content'),
        html.Pre(contents[0:200] + '...', style={
            'whiteSpace': 'pre-wrap',
            'wordBreak': 'break-all'
        })
    ])                

offline_rohini = pd.read_csv('rohini_khola_2021.csv')
offline_bgau = pd.read_csv('banjare_gau_2021.csv')
offline_channawa = pd.read_csv('channawa_2021.csv')
offline_dgau = pd.read_csv('d_gau_2021.csv')
offline_jaispur = pd.read_csv('jaispur_2021.csv')
offline_kalhanshangau = pd.read_csv('kalhanshgau_2021.csv')
offline_khadaicha = pd.read_csv('khadaicha_2021.csv')
offline_piprahawa = pd.read_csv('piprahawa_2021.csv')
offline_shikanpurwa = pd.read_csv('shikanpurwa_2021.csv')
# print(f"{offline_rohini.columns}-------------------->")
offline_df = [offline_rohini, offline_bgau, offline_channawa, offline_dgau, offline_jaispur, offline_kalhanshangau, offline_khadaicha, offline_piprahawa, offline_shikanpurwa]
# print(offline_df_roh.columns)
location_column_offline = ['Rohini Khola','Banjare Gau', 'Channawa','D-Gau','Jaispur','Kalhanshangau','Khadaicha','Piprahawa','Shikanpurwa']
cols_rename = ['SN','Date','Abs Pres (KPa)','Temp(°C)','Water Level(meters)']

all_offline_data = {}
def offline_data_transform(df,renamed_columns):
    df = df.iloc[:,:5]
    df.columns = cols_rename
    df['Water Level(meters)'] = abs(df['Water Level(meters)'])
    df['Date'] = pd.to_datetime(df['Date'])
    df['Month'] = df['Date'].dt.month
    df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])

    df['Date'] = df['Date'].dt.date
    df['Location'] = location_column_offline[i]
    # df.groupby(['name', 'id', 'dept'])['total_sale'].mean().reset_index()

    df = df.groupby(['Location','Month'], as_index=False)['Water Level(meters)'].mean().reset_index()
    # print(df)
    # all_offline_data[i] = df
    # print(df)

# for i in range(len(offline_df)):
#     offline_data_transform(offline_df[i],cols_rename)

# all_off_logger_df = pd.concat([all_offline_data[0],all_offline_data[1],all_offline_data[2],all_offline_data[3],
# all_offline_data[4],all_offline_data[5],
# all_offline_data[6],all_offline_data[7],all_offline_data[8]])
 
