# Name:     finalzie_data.py
# Function: Combine all refined data and generate the data table for analysis

import pandas as pd

# Read the school data from progress report cards data
schools = pd.read_csv('data/refined_progress.csv')

# Read crimes data that near to schools (<0.5km)
crimes_all = pd.read_csv('data/school_crimes.csv')

# Count total crimes near each school and add to the school data
crimes_by_school = crimes_all.groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Crimes':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

# Count number of crimes for different types near each school and add to the school data
# The meanings of different type IDs can be found in data/crime_types.csv

crimes_by_school = crimes_all[crimes_all['Crime_Type']==0].groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Thefts':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

crimes_by_school = crimes_all[crimes_all['Crime_Type']==1].groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Batteries':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

crimes_by_school = crimes_all[crimes_all['Crime_Type']==4].groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Assaults':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

crimes_by_school = crimes_all[crimes_all['Crime_Type']==7].groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Robberies':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

crimes_by_school = crimes_all[crimes_all['Crime_Type']==16].groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Weapon_Violations':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

crimes_by_school = crimes_all[crimes_all['Crime_Type']==20].groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Homicides':crimes_by_school.values})
schools = schools.merge(crimes, how='outer', on=['School_ID'])

# Add ACT Score data
act_all = pd.read_csv('data/refined_act.csv')
act = act_all[act_all['Year']==2016][['School ID','Composite']] \
    .rename(index=str, columns={'School ID':'School_ID', 'Composite':'ACT_Score'})
schools = schools.merge(act, how='outer', on=['School_ID'])

# Add college enrollment data
college = pd.read_csv('data/refined_college.csv') \
    .rename(index=str, columns={'School ID':'School_ID', 'Enrollment Pct':'College_Enrollment_Pct'})
schools = schools.merge(college, how='outer', on=['School_ID'])

# Add graduation rate data
grad = pd.read_csv('data/refined_graduation.csv') \
    .rename(index=str, columns={'SchoolID':'School_ID', '2017.1':'Graduation_Pct'})
schools = schools.merge(grad, how='outer', on=['School_ID'])

# Add SQRP rating data
level = pd.read_csv('data/ratings.csv')
schools = schools.merge(level, how='outer', on=['School_ID'])

# Finally, export the merged data to csv file
# Each row is a record of a school
# Each column is a variable
schools.to_csv('data/data_table.csv', index=False)
