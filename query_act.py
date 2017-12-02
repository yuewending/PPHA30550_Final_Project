# Name:     query_act.py
# Function: Download the data of average ACT scores.

import sys
import pandas as pd
import urllib.request as request
...
# Download the file 
request.urlretrieve('http://cps.edu/Performance/Documents/Datafiles/AverageACT_2016_SchoolLevel.xls', 'data/raw_act.xls')

'''
Format of the xls file:
* Data are in the sheet [act_schools_2001_to_2016]
* The first row is just the title, so ignore it.
* The second row is the column names
* The last two rows are footer notes, so ignore them.
* Cells with no values have a space character "*".
* Data contains the scores in different years.
* There are multiple columns but we only need column 0 (School ID) and 4 (Enrollment Pct of SY2016)
'''

raw_data = pd.read_excel('data/raw_act.xls', sheet_name='act_schools_2001_to_2016',
    header=0, skiprows=1, skipfooter=2)

# The data contains rows with different categories: overall, by genders or races. Only overall data are needed.
overall_data = raw_data[raw_data['Category']=='Overall']

# Columns are with mean scores and number of tested students for reding, math, science ... 
# We only need the composite mean score in this project 
refined_data = overall_data[['School ID', 'Year', 'Composite']]
refined_data.to_csv('data/refined_act.csv', index=False)