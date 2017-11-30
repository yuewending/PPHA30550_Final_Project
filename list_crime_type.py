
import pandas as pd
    
crimes = pd.read_csv('data/refined_crime_sy2016.csv')
type_crime = []
type_id = []

for index_c, crime in crimes.iterrows():
    
    if crime['Primary Type'] not in type_crime:
        type_id.append(len(type_crime))
        type_crime.append(crime['Primary Type'])
    
    if index_c % 10000 == 0:
        print("Finish mapping crime %d/%d" % (index_c, len(crimes)))
        
pd.DataFrame({'Type ID': type_id, 'Type': type_crime}).to_csv('data/crime_types.csv', index=False)