import sys
import pandas as pd
import urllib.request as request
...
# Download the file 
request.urlretrieve('http://cps.edu/Performance/Documents/Datafiles/AverageACT_2016_SchoolLevel.xls', 'data/raw_act.xls')

# Import raw csv data with all schools
raw_data = pd.read_excel('data/raw_act.xls', sheet_name='act_schools_2001_to_2016',
    header=0, skiprows=1, skipfooter=2)

overall_data = raw_data[raw_data['Category']=='Overall']
refined_data = overall_data[['School ID', 'Year', 'Composite']]
refined_data.to_csv('data/refined_act.csv', index=False)