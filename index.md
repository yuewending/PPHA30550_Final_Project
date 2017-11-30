# How Neighborhood Safety Affect High School Performances?
Final Project of Data Anaysis for Course PPHA30550

**Students:** Xiaofan Liu (#1214xxxx) and Yuewen Ding (#12149112)

**Date:** Nov. 30, 2017

## Targets

Students’ decisions making process on future education is influenced by a combination of factors, including but not limited to their past academic achievements, quality of schools, interests and external environment. The key question for policy makers is how we could improve the education environment in the most cost-effective way. Based on a survey conducted in Ohio, safety is the top one concern when choosing schools for their children. It is important to figure out following questions: Does safety (crime rate nearby the location of a school) affect school performances that are considered for choices making? If so, to what extent? Does it have the same effect on students in different aspects (such as ACT score, college enrollment) or by different types of crimes? The targets of this project is to understand the data correlations between performances Chicago high schools and the safety (crime rates) of their locations. All data used in the study is for the 2016-2017 school year (Sep. 1, 2016 to Aug. 31, 2017). The school performance data are 181 high schools in Chicago, and the crime data are case records of the Chicago city.

## Data Preparation

The scripts that were used to prepare all data set areput in this folder, and data files are stored in the [`data`](https://github.com/yuewending/PPHA30550_Final_Project/tree/master/data) folder.

### Performance Data of High Schools

The performance data are from several different portals but they are all from [Chicago Public Schools (CPS)](http://www.cps.edu/) originally. CPS assign each school a unique **School ID** in all different data sets and studies, so it helps us combine variables from multiple files by matching the **School ID**.

#### High School Progress Report Cards

This is an annual report from each CPS high school, including the summary how the school is doing. However, most of the variables were given as ranks or percentiles, which is not easily to be used as a straightforward quantative indicators. We use the data set to extract the basic information of the schools: **Schoo ID, Name, Latitude, Longitude.** Another variable we use from it is the safety assessment obtained from parents/students survey. The safety descriptions are in the options of "VERY WEAK", "WEAK", "NEUTRAL", "STRONG" and "VERY STRONG", which will be converted into numbers 1~5, and the higher the better safety assessment.

**Step:** run the python script "`query_progress.py`" in this folder

**Output files:** 
  1. `raw_progress.csv` The raw data downloaded via Chicago Data Portal.
  2. `refined_progress.csv` The refined data file containing target variables only.
  3. `school_id.csv` an one-column list containing all School IDs.

#### High School Assessment Reports and Metrics

CPS provides many useful data sets via its [School Data](http://cps.edu/SchoolData/Pages/SchoolData.aspx) page. These data sets are provided in Excel format. We downloaded datasheet and use Python/Pandas to extract the columns that we need, as well as the School ID column for matching. We used three files in this study with variables: **"11th Grade ACT Scores", "5-year Graduation Percentages" and "After 2-Year College Enrollment Percentages".**

**Step:** run the python script "`query_act.py`", "`query_graduation.py`","`query_college.py`" in this folder

**Output files:** 
  1. `raw_[XXX].xls` The raw data downloaded from CPS.
  2. `refined_[XXX].csv` The refined data file containing target variables only.


### Crime Rates



### Step 1: Obtaining List of US High Schools

