# Name:     query_progress_report.py
# Function: Filter out targeted HIGH schools (rows) and variables (columns) from raw data.

import pandas as pd
import numpy as np
import urllib.request as request

# Download the file 
request.urlretrieve('https://data.cityofchicago.org/api/views/cp7s-7gxg/rows.csv?accessType=DOWNLOAD', 'data/raw_progress.csv')

# Import raw csv data with all schools
raw_data = pd.read_csv('data/raw_progress.csv')
print("Import CSV file of [%d] schools" % (len(raw_data)))

# Filter out high schools
hs_data = raw_data.loc[raw_data['Primary_Category'] == 'HS']
print("Number of high schools = %d" % (len(hs_data)))

# Define a function to convert safety text into number from 1 to 5, or NaN
def set_safety_level(row):
    
    safety_levels = {
        'NOT ENOUGH DATA' : np.nan,
        'VERY WEAK'   : 1,
        'WEAK'        : 2,
        'NEUTRAL'     : 3,
        'STRONG'      : 4,
        'VERY STRONG' : 5
    }
    
    return safety_levels[row['School_Survey_Safety']]

# Apply the fuction to add a new column for safety level values
hs_data['Safety_Level'] = hs_data.apply (lambda row: set_safety_level(row),axis=1)

# Select columns that we need for later analysis

selected_columns = [
    'School_ID',
    'Short_Name',
    'Safety_Level',
    'School_Latitude',
    'School_Longitude'    
]

refined_data = hs_data[selected_columns]

# Dump refined data
refined_data.to_csv('data/refined_progress.csv', index=False)

# Dump school IDs only (no header)
refined_data['School_ID'].to_csv('data/school_id.csv', index=False, header=False)