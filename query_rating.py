# Name:     query_rating.py
# Function: Obtain school ratings based on IDs.

import time
import requests
import pandas as pd
from bs4 import BeautifulSoup as bs

# URL format of target links
url_prefix = 'http://schoolinfo.cps.edu/schoolprofile/SchoolDetails.aspx?SchoolId='

# Get all school IDs
with open("data/school_id.csv", "r") as f:
    schools = f.read().split('\n')

# List for converting Levels text to number
levels = ['None', 'Level 3', 'Level 2', 'Level 2+', 'Level 1', 'Level 1+']

# Build empty lists
data_id = []
data_level = []

# Query all levels
for id in schools:
    if id == '':
        continue
    
    # wait three second to do each query to avoid the website to block us
    time.sleep(3)
    
    # get the page and parse its html content
    html_doc = requests.get(url_prefix + id)
    soup = bs(html_doc.text, 'html.parser')
    
    # find the target span element with the specific id
    span = soup.find('span', {'id':'ctl00_ContentPlaceHolder1_lbOverallRating2'})
    
    # some schools doen't have a valid rating, so skip them
    if span is None:
        continue
    
    # get the text of level and convert it to be the number from 1 to 5
    
    level = span.text
    ilevel = levels.index(level)
    
    # print the debug information and append to lists
    print("School=%s\tLevel=%d" % (id, ilevel))
    data_id.append(id)
    data_level.append(ilevel)
    

# Dump the data to CSV file
df = pd.DataFrame({'School_ID': data_id, 'Level': data_level})
df.to_csv('data/ratings.csv', index=False)
