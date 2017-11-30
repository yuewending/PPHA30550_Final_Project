
import pandas as pd

schools = pd.read_csv('data/refined_progress.csv')

crimes_all = pd.read_csv('data/school_crimes.csv')

crimes_by_school = crimes_all.groupby(['School_ID']).size()
crimes = pd.DataFrame({'School_ID':crimes_by_school.index, 'Total_Crimes':crimes_by_school.values})
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

act_all = pd.read_csv('data/refined_act.csv')
act = act_all[act_all['Year']==2016][['School ID','Composite']] \
    .rename(index=str, columns={'School ID':'School_ID', 'Composite':'ACT_Score'})
schools = schools.merge(act, how='outer', on=['School_ID'])

college = pd.read_csv('data/refined_college.csv') \
    .rename(index=str, columns={'School ID':'School_ID', 'Enrollment Pct':'College_Enrollment_Pct'})
schools = schools.merge(college, how='outer', on=['School_ID'])

grad = pd.read_csv('data/refined_graduation.csv') \
    .rename(index=str, columns={'SchoolID':'School_ID', '2017.1':'Graduation_Pct'})
schools = schools.merge(grad, how='outer', on=['School_ID'])

level = pd.read_csv('data/ratings.csv')
schools = schools.merge(level, how='outer', on=['School_ID'])

schools.to_csv('data/data_table.csv', index=False)
