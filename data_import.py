import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import time, sched

import dash_html_components as html

import calendar

url= "https://kc.humanitarianresponse.info/api/v1/data/669773.json"
auth = HTTPBasicAuth('gw_monitoring', 'gwmonitor@2020')




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
    # gw_df = pd.read_json(download.text)   
    if len(gw_df.columns) != 35:
        #     return html.Div([html.H1("ERROR: With fetching the data. Please check later")])
            df = pd.DataFrame()
        #     df = pd.read_csv('updated_data.csv')  
            print("ERROR")
    else:
        gw_df.columns = ['_notes',
       'Measurement_of_tape_ent_point_MP_in_m',
       'Notes', '_tags', '_xform_id_string',
       'meta/instanceID', 'gw_level_from_mp', 'end',
       'gw_level',
       'Well_photo_Use_the_ed_measurement_point',
       'mp_in_m', 'start', '_attachments', '_version_',
       '_status', '__version__', 'today',
       'sw_bk_well_no',
       'Enumerator Name',
       'Geo_location', '_validation_status',
       '_uuid', 'well_type', 'formhub/uuid',
       'District', '_submission_time',
       '_geolocation', '_submitted_by',
       'wet_point_measruement_on_tape', 'deviceid',
       'measurement_point_cm', '_id',
       'bk_dw_no',
       'well_no_sw_bardiya',
       'well_no_dw_bardiya']
        gw_df = gw_df[['Enumerator Name','Geo_location','District',
        'well_type','sw_bk_well_no','bk_dw_no','well_no_sw_bardiya','well_no_dw_bardiya','measurement_point_cm',
        'Measurement_of_tape_ent_point_MP_in_m', 'wet_point_measruement_on_tape','gw_level',
        'Notes','today']]
        # print(gw_df)
        df = gw_df.copy()   
        df = gw_df.iloc[5:]
            # print(gw_df[i])      
        df.to_csv('updated_data.csv')
    return df 

gw_df = download_data()


### Data to map the values
def map_data(well_number):
        df = pd.read_csv('updated_data.csv')
        df['well_no'] = (df['sw_bk_well_no'].combine_first(df['bk_dw_no']).combine_first(df['well_no_sw_bardiya']).combine_first(df['well_no_dw_bardiya']))
        ## onvertt he today data to date    
        df['today'] = pd.to_datetime(df['today'])
        df['Month'] = df['today'].dt.month
        # print(df['Month'])
        df['Month'] = df['Month'].apply(lambda x: calendar.month_abbr[x])
        cols = ['well_no','Month','gw_level']
        df = df[cols]
        x = df[df['well_no'].isin([well_number])]
        # print(x)
        return x


#banke SW data


banke_sw = gw_df[(gw_df['District']=="Banke") & (gw_df['well_type'] == 'sw')]
banke_sw= banke_sw[['Enumerator Name','Geo_location','District',
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