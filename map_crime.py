# wget -O crime_2017.csv 'https://data.cityofchicago.org/api/views/d62x-nvdr/rows.csv?accessType=DOWNLOAD'
# wget -O crime_2016.csv 'https://data.cityofchicago.org/api/views/kf95-mnd6/rows.csv?accessType=DOWNLOAD'

import pandas as pd
'''
data = pd.read_csv('data/crime_2016.csv', 
    usecols = ['Case Number','Date','Primary Type','Arrest','Latitude','Longitude'],
    parse_dates = ['Date'])

refined_data = data[data['Date']>'2016-08-31']
refined_data.to_csv('data/refined_crime_2016.csv', index=False)

data = pd.read_csv('data/crime_2017.csv', 
    usecols = ['Case Number','Date','Primary Type','Arrest','Latitude','Longitude'],
    parse_dates = ['Date'])

refined_data = data[data['Date']<'2017-09-01']
refined_data.to_csv('data/refined_crime_2017.csv', index=False)


crime2016 = pd.read_csv('data/refined_crime_2016.csv')
crime2017 = pd.read_csv('data/refined_crime_2017.csv')
crimes = pd.concat([crime2016, crime2017])
crimes.to_csv('data/refined_crime_sy2016.csv', index=False)

'''

import math

def distance(origin, destination):
    lat1, lon1 = origin
    lat2, lon2 = destination
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = radius * c

    return d
    
crimes = pd.read_csv('data/refined_crime_sy2016.csv')
schools = pd.read_csv('data/refined_progress.csv')
type_crime = []

crime_type = []
crime_id = []
school_id = []
distances = []

for index_c, crime in crimes.iterrows():
    coord_crime = (crime['Latitude'], crime['Longitude'])
    
    if crime['Primary Type'] not in type_crime:
        type_crime.append(crime['Primary Type'])
    
    itype = type_crime.index(crime['Primary Type'])
    
    for index_s, school in schools.iterrows():
        school_crime = (school['School_Latitude'], school['School_Longitude'])
        dist = distance(coord_crime, school_crime)
        
        if dist < 0.5:
            crime_type.append(itype)
            crime_id.append(crime['Case Number'])
            school_id.append(school['School_ID'])
            distances.append(dist)
    
    if index_c % 1000 == 0:
        print("Finish mapping crime %d/%d" % (index_c, len(crimes)))
        
        df = pd.DataFrame({'Crime_Type': crime_type, 'School_ID': school_id, 'Crime_ID': crime_id, 'Distance': distances})
        df.to_csv('data/school_crimes.csv', index=False)
        

pd.DataFrame({'Type ID': range(len(type_crime)), 'Type': type_crime}).to_csv('data/crime_types.csv', index=False)
