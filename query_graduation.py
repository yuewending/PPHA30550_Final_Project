import sys
import pandas as pd
import urllib.request as request

# Download the file 
request.urlretrieve('http://cps.edu/Performance/Documents/DataFiles/Metrics_CohortGraduationDropout_SchoolLevel_2017.xls', 'data/raw_graduation.xls')

# Import raw csv data with all schools
data = pd.read_excel('data/raw_graduation.xls', sheet_name='School 5 Year Cohort Rates',
    header=0, skiprows=1, usecols=[0,16], na_values=" ")

data.dropna().to_csv('data/refined_graduation.csv', index=False)