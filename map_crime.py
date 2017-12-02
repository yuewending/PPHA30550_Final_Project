# Name:     query_progress_report.py
# Function: Filter out targeted HIGH schools (rows) and variables (columns) from raw data.

import pandas as pd
import urllib.request as request
import math

# Download files. Because we want to use the crime records in SY2016, so we need to use data from two calendar years
# Warning: each file is about 50~60MB, so this step takes some minutes.
request.urlretrieve('https://data.cityofchicago.org/api/views/kf95-mnd6/rows.csv?accessType=DOWNLOAD', 'data/crime_2016.csv')
request.urlretrieve('https://data.cityofchicago.org/api/views/d62x-nvdr/rows.csv?accessType=DOWNLOAD', 'data/crime_2017.csv')

# Refine data with columns that we need
# Warning: each file has more than 200K records, so this step takes several minutes
data = pd.read_csv('data/crime_2016.csv', 
    usecols = ['Case Number','Date','Primary Type','Arrest','Latitude','Longitude'],
    parse_dates = ['Date'])

# Filter out records earlier than 08/31, and save the refined data
refined_data = data[data['Date']>'2016-08-31']
refined_data.to_csv('data/refined_crime_2016.csv', index=False)

# Refine rows for data of 2017
data = pd.read_csv('data/crime_2017.csv', 
    usecols = ['Case Number','Date','Primary Type','Arrest','Latitude','Longitude'],
    parse_dates = ['Date'])

# Filter out records later than 09/01, and save the refined data
refined_data = data[data['Date']<'2017-09-01']
refined_data.to_csv('data/refined_crime_2017.csv', index=False)

# Import saved data again and combine them
# Why didn't we directly combine them? Because each step in this script takes long time to finish,
# so we ran it step by step and save and resume midpoint data.
crime2016 = pd.read_csv('data/refined_crime_2016.csv')
crime2017 = pd.read_csv('data/refined_crime_2017.csv')
crimes = pd.concat([crime2016, crime2017])
crimes.to_csv('data/refined_crime_sy2016.csv', index=False)

# Define a function for gegraphic distance compute
# this function returns the "biggest-circle distance" of two groups of lat/lon on the earth

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km, presumed radius of earth
    
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c
    
    return d

# Read all crime records and schools with lat/lon variables
crimes = pd.read_csv('data/refined_crime_sy2016.csv')
schools = pd.read_csv('data/refined_progress.csv')

# Save the texts of different crimes
type_crime = []

# List to construct the pandas dataframe
crime_type = [] # type ID, an integer number
crime_id   = [] # case ID, text string
school_id  = [] # school ID, text string
distances  = [] # float number

# The next step is to map each crime case to the school located within 0.5km
# Warning: this step takes really long time to finish!!! ~1.5 hours

# Loop over all crime case records
for index_c, crime in crimes.iterrows():
    # Prepare crime lat/lon location
    coord_crime = (crime['Latitude'], crime['Longitude'])
    
    # If this is the first time getting the type text, append it.
    if crime['Primary Type'] not in type_crime:
        type_crime.append(crime['Primary Type'])
    
    # Return the integer ID of crime types from the text
    itype = type_crime.index(crime['Primary Type'])
    
    # Loop over all school locations
    for index_s, school in schools.iterrows():
        # Prepare school lat/lon location
        school_crime = (school['School_Latitude'], school['School_Longitude'])
        
        # Calculate the distance between the crime and school locations
        dist = distance(coord_crime, school_crime)
        
        # If the distance is smaller than 0.5km, save this matched relation
        if dist < 0.5:
            crime_type.append(itype)
            crime_id.append(crime['Case Number'])
            school_id.append(school['School_ID'])
            distances.append(dist)
    
    # report the progress for every 1000 crimes (~30 seconds)
    if index_c % 1000 == 0:
        print("Finish mapping crime %d/%d" % (index_c, len(crimes)))
        
        # save the intermediate results to files
        df = pd.DataFrame({'Crime_Type': crime_type, 'School_ID': school_id, 'Crime_ID': crime_id, 'Distance': distances})
        df.to_csv('data/school_crimes.csv', index=False)
        
# Save the ID/Text of crime types information
pd.DataFrame({'Type ID': range(len(type_crime)), 'Type': type_crime}).to_csv('data/crime_types.csv', index=False)
