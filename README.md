# Correlation Between Performance and Safety of High Schools
Final Project of Data Anaysis for Course PPHA30550

### Targets

The targets of this project is to understand the data correlations between performances high schools and the safety (crime rates) of their locations. The study is conducted based on the school profiles and crime records on three resolutions: states, cities and districts.

### Data sources:

#### Performances of High Schools

* Data of high schools are from the GreatSchools website https://www.greatschools.org/, which is a nonprofit project helps parents to choose high schools for their children by providing different indicators of school qualities. The information include basic profile (name, address, level ...), academic reports (scores, graduation ratio, attending college ratio ...) and other school climate data (incomes, races, ...).

#### Crime Rates

Crime rates are obtained at three levels (resolutions): state, city and district.

* **State** crime rates are from **Uniform Crime Reporting (UCR) Statistics** https://www.ucrdatatool.gov/ with the "state and national estimates" data portal for the year 2014. The CSV formatted raw data file is downloaded manually.

* **City** crime rates are also from **URC Statistics** https://www.ucrdatatool.gov/ with the "Local law enforcement agencies" data portal for the year 2014. Cities of four states (NY, MA, CA, IL) are used for this study. The CSV formatted raw data file is downloaded manually.

* **District** crime rates are obtained for four cities (New York City, Chicago, Boston, Los angeles) with different city data portals.
  * New York City
  * Chicago
  * Boston
  * Los angeles

### Step 1: Obtaining List of US High Schools

There's no direct export of table or database file from the greatshools.org, instead, the variables of each school are provided in a seperated page. The links are in the format of "/texas/lubbock/19361-Canyon-Lakes/" combined with the state name, city name, an internal ID and the school name. Therefore, we need to obtain the list of URL links of the schools we care for.

The list can be obtained via its search engine via the GET method. (https://www.greatschools.org/search/search.page) For this project, we select all public high school for the filtering (private school data are not provided). The results from the search are paged, so we need to first obtain the number of pages, and then query the page one by one, and finally extract the school links from each result page. The PYTHON code is written in,
```
step1_school_list.py
```
And this code is to finish four tasks:
* Get the number of pages from the search
* Download all HTML pages
* Obtain school links based on the CSS class name
* Dump all links in the file **data/school_links.txt**

### Step 2: Download School Performace Data

On each page, the variables are within DIV elements with different CSS class names. We checked the source code of the web page, and extract the information based on such characteristics. The PYTHON code is written looping over all links and extract the information to make a CSV table.
```
step1_school_list.py
```
And this code is to finish three tasks:
* Download a web page from links in **data/school_links.txt**
* Parse the web page and find all variables that we need
* Write out variables in the CSV table format at **data/school_performance.csv**.

### Step 3: Process of State Crime Data and Correlation Analysis

Download the raw data file and save it at **data/crime_states.csv**

### Step 4: Process of City Crime Data and Correlation Analysis

Download the raw data files and save them at **data/crime_XX.csv** (XX are for CA, MA, NY, IL)

### Step 5: Process of District Crime Data and Correlation Analysis
