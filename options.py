import pandas as pd

import dash_leaflet as dl
import dash_leaflet.express as dlx

tubewell_options = [{'label': 'Deep Tubewell', 'value': 'dt'},
                        {'label': 'Shallow Tubewell', 'value': 'st'},
                        # {'label': 'Both Shallow and Deep Tubewell', 'value': 'both'}
                        ]

# tubewell locations
df = pd.read_excel('data/preloaded_data/updated_well_data.xlsx')
print(df.columns)
# print(df.columns)
df_dptw = pd.read_excel('data/preloaded_data/updated_well_data.xlsx', sheet_name= 'Deep tube wells')
df_both = pd.concat([df,df_dptw])
# print(df.columns)
st_location_options = [{'label': i, 'value': i} for i in df['Location ']]
dt_location_options = [{'label': i, 'value': i} for i in df_dptw['Location ']]
# print(df['Location '].unique())
# print(st_location_options)
# print(location_options)

## Data for yearly water level 
df_data = pd.read_csv('data/preloaded_data/all_wells_clean_tall.csv')
df_2015 = pd.read_excel('data/preloaded_data/historical_data.xlsx',sheet_name = '2015')
df_2014 = pd.read_excel('data/preloaded_data/historical_data.xlsx',sheet_name = '2014')
# df_2015_stw = pd.read_excel('data/preloaded_data/Water table data of Banke/Banke/cleaned_data/cleaned_xlsx/df_2015.xlsx')
# df_2015_dtw = pd.read_excel('data/preloaded_data/Water table data of Banke/Banke/cleaned_data/cleaned_xlsx/df_2015.xlsx',
# sheet_name= 'df_2015_dtw')
# df_2014_stw = pd.read_excel('data/preloaded_data/Water table data of Banke/Banke/cleaned_data/cleaned_xlsx/df_2014.xlsx')
# df_2014_dtw = pd.read_excel('data/preloaded_data/Water table data of Banke/Banke/cleaned_data/cleaned_xlsx/df_2014.xlsx',
# sheet_name= 'df_2014_dtw')
# print(df_2015_stw.columns)

# modify the data to meet requirements
def modify_df(dataframe,well_no,selected_year):
    df = dataframe[dataframe['well_no'].isin([well_no]) & dataframe['year'].isin([selected_year])]
    # print(df)
    if not df.empty:
        df = df.loc[:,['month','value']]
        df.columns = ['Months','gw_level']

    else:
        df = pd.DataFrame()
    return df

# selection = df.loc[:2,['Name', 'Age', 'Height', 'Score']]

# Option for the drop downs

all_options = {
    'st': df['Location '].tolist(),
    'dt': df_dptw['Location '].tolist(),
}
both_options = {
     'both': df_dptw['Location '].tolist() + df['Location '].tolist()
}


# Converting data to dictinoary to use in the maps
dicts_swt = df.to_dict('rows')
dicts_dwt = df_dptw.to_dict('rows')
dicts_both = df_both.to_dict('rows')

swt_geojson = dlx.dicts_to_geojson(dicts_swt, lon="Longitude", lat = 'Latitude')  # convert to geojson
dwt_geojson = dlx.dicts_to_geojson(dicts_dwt, lon="Longitude", lat = 'Latitude')  # convert to geojson
both_geojson = dlx.dicts_to_geojson(dicts_both, lon="Longitude", lat = 'Latitude')  # convert to geojson


## Years options
years = []
for i in range(1996,2016):
    years.append(i)
years_dict = {str(year): str(year) for year in years}
# print(years_dict)
# print(years)
