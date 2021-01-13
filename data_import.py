import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import time, sched

import dash_html_components as html



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
       
    # gw_df = pd.read_json(download.text)   
         
    gw_df.columns = ['_notes',
       'Measurement_of_tape_ent_point_MP_in_m',
       'Notes', '_tags', '_xform_id_string',
       'meta/instanceID', 'end', 'gw_level',
       'Height_of_measuremen_in_measurement_unit',
       'Well_photo_Use_the_ed_measurement_point',
       'start', '_geolocation', '_attachments', '_version_', '_status',
       '__version__', 'today', 'sw_bk_well_no',
       'Enumerator Name',
       'location_image',
       'Geo_location', '_validation_status',
       '_uuid', 'well_type', 'formhub/uuid',
       '_submission_time', 'District',
       '_submitted_by', 'deviceid', '_id',
       'bk_dw_no',
       'well_no_sw_bardiya','well_no_dw_bardiya']
    gw_df = gw_df[['Enumerator Name','Geo_location','District',
        'well_type','sw_bk_well_no','bk_dw_no','well_no_sw_bardiya','well_no_dw_bardiya','gw_level',
        'Height_of_measuremen_in_measurement_unit',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]
        # print(gw_df)
    df = gw_df.copy()   
    df = gw_df.iloc[4:]
            # print(gw_df[i])      
    df.to_csv('updated_data.csv')
    return df 

gw_df = download_data()





#banke SW data


banke_sw = gw_df[(gw_df['District']=="Banke") & (gw_df['well_type'] == 'sw')]
banke_sw= banke_sw[['Enumerator Name','Geo_location','District',
        'well_type','sw_bk_well_no','gw_level',
        'Height_of_measuremen_in_measurement_unit',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]




banke_dw = gw_df[(gw_df['District']=="Banke") & (gw_df['well_type'] == 'dt')]
banke_dw = banke_dw[['Enumerator Name','Geo_location','District',
        'well_type','bk_dw_no','gw_level',
        'Height_of_measuremen_in_measurement_unit',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]



bardiya_sw = gw_df[(gw_df['District']=="Bardiya") & (gw_df['well_type'] == 'sw')]


bardiya_sw = bardiya_sw[['Enumerator Name','Geo_location','District','well_type','well_no_sw_bardiya','gw_level',
        'Height_of_measuremen_in_measurement_unit','Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]

    


bardiya_dw = gw_df[(gw_df['District']=="Bardiya") & (gw_df['well_type'] == 'dt')]
bardiya_dw = bardiya_dw[['Enumerator Name','Geo_location','District',
        'well_type','well_no_dw_bardiya','gw_level',
        'Height_of_measuremen_in_measurement_unit',
        'Measurement_of_tape_ent_point_MP_in_m',
        'Notes']]



# print(gw_df)
print("JOB DONE")