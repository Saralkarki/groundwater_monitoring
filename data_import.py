import requests
from requests.auth import HTTPBasicAuth
import pandas as pd
import time, sched



url= "https://kc.humanitarianresponse.info/api/v1/data/669773.json"

auth = HTTPBasicAuth('gw_monitoring', 'gwmonitor@2020')
# files = {'filename': open('filename.txt','rb')}
def download_data():
    download = requests.get(url, auth=auth )
    
    col_names = ['Enumerator Name','Geo_location','Municipality','village_name','ward','well_type','well_no_st','well_no_dt','gw_level','measurement_unit']
    df = pd.read_csv('updated_data.csv')
    
            
    gw_df = pd.read_json(download.text)
    # print(len(gw_df))

    if not 'Main_group/location_details/well_no_dt' in gw_df.columns:
        # print('NO DT')
        gw_df['well_no_dt'] = ''
    if not 'Main_group/location_details/well_no_sw' in gw_df.columns:
        # print('NO ST')
        gw_df['well_no_st'] = ''
    if len(gw_df) != 0:   
        print(gw_df.columns)   
        gw_df.columns = ['_notes', '_tags', '_xform_id_string', 'meta/instanceID','gw_level', '_geolocation',
       'Municipality', '_status', 'uuid','today', 'Enumerator Name',
       'Geo_location', '_validation_status','start_time', '_uuid', 'well_type',
       '_submitted_by', 'village_name','device_id', 'ward', '__version__',
       '_submission_time', '_attachments','measurement_unit', 'end_time',
       'well_no_st', '_id','well_no_dt']
        gw_df = gw_df[['Enumerator Name','Geo_location','Municipality','village_name','ward','well_type','well_no_st','well_no_dt','gw_level','measurement_unit']]
        print(gw_df)
        df = gw_df.copy()    

            # print(gw_df[i])      
        df.to_csv('updated_data.csv')
        # print(df)
        return df
    else: 
        df = pd.read_csv('updated_data.csv')  
        return df

gw_sw = download_data()



gw_df = pd.read_csv('updated_data.csv')

# print(gw_df)
print("JOB DONE")