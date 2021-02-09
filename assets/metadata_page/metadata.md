# Introduction, user instructions, and meta-data 

This activity is funded by USAID as part of the 'CSISA III: COVID Resilience Response' project. This activity is lead by CIMMYT International Maize and Wheat Improvement Center in coordination with the Groundwater Resources Development Board of Nepal (GWRDB) and supported by project partners International Water Management Institute (IWMI), Texas A&M University, and Cornell University.

## How to use? Quick Summary

- This is the beta version of the dashboard and is designed to provide rapid access to the data that we are collecting and for soliciting rapid feedback about the data collection and visualization. We aim to upgrade this dashboard in the near future with a richer feature set.
- You are currently on the home page. Here we provide an overview of this project activity and provide further background information about the displayed data, data collection methods, and the local aquifer.
- The real-time monitoring page provides and overview of recently collected data through different monitoring methods (see below for more information). You can toggle the map to display different monitoring methods and click on the wells to see the data collected for each specific location and methods.
- The database page provides access to the detailed data that has been collected and you can download it in CSV format.
- The Historical data page contains data that has been collected by the GWRDB since the year 2000. Note that this data has not been cleaned, but it can be used to obtain a better feel for the groundwater level fluctuations that are typical in the region.

## Background
Nepal's Terai has an estimated 8,800 MCM of groundwater reserves, based on assessments carried out in the 1970s and 1980s, and abstraction of groundwater from these aquifers has steadily increased with irrigation being the main water user. Electrification, promotion of solar pumps, increasing private investments in diesel pump irrigation and growing industrial water use are progressively increasing the demand for groundwater in Nepal's Terai and localized reports of groundwater depletion have started to surface.

Monitoring the water levels of the Terai's aquifers is thus critical to ensure that groundwater development does not deplete the resource beyond sustainable limits. While the responsibilities of groundwater management are currently spread across different governmental bodies, the GWRDB retains a mandate for groundwater monitoring activities that are to be implemented through its branch offices.  

Specifically, Nepal's GWRDB has the following main objectives:

1. Identification of groundwater potential area in the Terai (shallow and deep aquifer) through geophysical survey and investigation tubewells.
2. Exploitation of shallow and deep aquifer in the Terai for irrigation and drinking purpose.
3. Develop technical manpower related to groundwater field.
4. Regular monitoring of existing investigation tubewells for water level fluctuation, groundwater reserves and water quality.
5. Study and investigation of mountain and Karst aquifer.
6. Groundwater Resources Development Board (GWRDB), located at Babarmahal, Kathmandu is responsible to carry out above mentioned activities through its 8 branch offices. 

Groundwater Field Offices are located at Biratnagar, Lahan, Mahottari, Birganj, Butwal, Dang, Nepalganj and Dhangadhi.

As of now, each of the branch offices employs one data collector per overseen district who measures the groundwater level of ca. 20 wells per district on a monthly basis. These measurements are then transcribed from pen and paper into an excel worksheet that is stored with the GWRDB.

The current procedure has three major shortcomings: 

1. The process introduces a time lag for data availability and potential errors in transcribing the data. 
2.  The data is not easily accessible to a wider audience of interested users, limiting the use of these data for research and development planning.
3. The data is not easily visualizes for mapping of groundwater levels in space and time and for processing into information for different use cases.

## Objective

The goal of this project activity is to pilot an open data system for groundwater data in Banke district with the aim to develop a system that can be scaled to other districts of Nepal.

The sub-objectives include: 
1. Evaluate the efficacy of different approaches for automatizing data groundwater measurements and data collection (Manual, ODK-based, offline loggers, online loggers).
2. Develop a dashboard that displays the groundwater monitoring data catering to different use cases. 
3. Provide access to  groundwater level data and important auxiliary information for users of the dashboard.

## Dashboard description

The dashboard is being developed on a continuous basis. This first version is aimed to provide rapid support and real-time visualization for the ongoing data collection efforts. In the background we are constantly developing the feature set of the dashboard based on experience and user feedback. We therefore kindly invite anybody to get in touch with us and provide any feedback or demands for additional features. 

The dashboard is divided into three different components: 
1. The real-time monitoring data
2. A spreadsheet with more information about each measurement and the possibility for downloading the data.
2.  An overview of the historical data for Banke district.

### Real-time monitoring

This section displays in real-time the data that is being collected for this specific project during the year 2021. To evaluate different data collection approaches, this section categorizes data points into three different categories:

1. ODK-based data collection.
	- This method replaces the manual data entry with ODK-supported data entry on a tablet. After measuring the water level, the data collector immediately enters the data in a survey form on his tablet which is immediately send to the cloud and processed. Data collection takes place on a monthly basis.
2. Offline data loggers.
	- This method uses 10 low-cost offline data loggers to record daily water levels. The data loggers need to be read out and uploaded to the data base manually, which takes place on a 2-weekly basis.
3. Online data loggers (not operational because imports are delayed due to COVID19)
	- Online data loggers transmit information to the cloud in real-time by using the cellular network. Powered through a small solar panel, the system ready the water level and immediately transmits the information to the online survey from where it is further processed and visualized.

### Database

This section shows the uploaded data. It includes all the variables that are submitted to the server including location, well number, name of data collector, date, measurement details and the final groundwater level for the ODK based data, and groundwater level for the offline loggers. By clicking the "export" button the whole dataset can be downloaded. Note, that this dataset has not been screened for errors so use with caution. 

### Historical data

These data have been manually collected and curated since the year 2000. However, some years and data points are missing and typos have not been fixed yet. You can click both on the wells in the map or on the graph in the bottom to select and de-select wells of interest. Below the graphs you can select the year of interest.

### Well selection

The GWRDB oversees ~20 shallow and ~5 deep tubewells for monitoring purposes per district. This pilot did not establish additional wells but uses the existing ones. The offline wells were selected in order to capture the North-South and East-West gradient. However, some wells were not practical to install and had to be exchanged for more feasible alternatives.

### Geographical setting and hydro-geological Characteristics

Nepal's Terai belongs to the Northernmost section of the Indo-Gangetic Plains that stretch from the foothills of the Himalayas to the Ganges Rivers in the South at around 100 masl. The aquifers thus belong to the Indo-Gangetic Basin alluvial aquifer. General characteristics of the aquifers can, for example, be found in Bonsor et al. (2017) https://doi.org/10.1007/s10040-017-1550-z. A typical cross section of the Terai aquifer looks like the following (with yellow being coarser sand layers of good aquifer material, Bonsor et al. 2017):

![Terai Aquifer Schematic](terai_aquifer.webp) 

</br>


Nepal's Terai aquifers are comprised of alluvial and poorly sorted aquifer material. Several layers of aquifer material are intersected by several layers semi-confining clay layers. Water levels for aquifers range from 0 to 10 mbgl with an average of 4.5 mbgl. The following map has been produced by the GWRDB based on the water level measurements of the GWRDB/UNDP tubewells of 1993: 

![Aquifer Characteristics Map Banke](banke_hydrogeo.png) 

</br>
</br>

## Contact

In case you should have any question kindly get in touch and contact Anton Urfels at anton.urfels@wur.nl. 