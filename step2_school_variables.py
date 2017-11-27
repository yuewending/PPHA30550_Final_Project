import time
import requests
from bs4 import BeautifulSoup as bs

def get_school_grade(soup, title):
    
    link = soup.find('a', {'data-ga-click-label':title})
    if link is None:
        return ''
    
    span = link.find('span', {'class': 'circle-rating--xtra-small'})
    if span is None:
        return ''
    
    return span.text.strip().split('/')[0]

def parse_school_page(link):
    
    # query shchool page and build html object 
    url = 'https://www.greatschools.org/' + link
    html_doc = requests.get(url + "1")
    soup = bs(html_doc.text.encode('ascii','ignore'), 'html.parser')
    
    # parse basic information
    school = {}
    school['Name'] = soup.find('h1', class_='school-name').text
    school['Address'] = soup.find('div', class_='school-contact__item school-contact__address').find('span', class_='content').text
    school['Zipcode'] = school['Address'][-5:]
    
    school['College'] = get_school_grade(soup, 'College readiness')
    school['Progress'] = get_school_grade(soup, 'Academic progress')
    
    # obtain test scores
    scores = soup.find_all('div', class_='test-score-container clearfix')
    
    for score in scores:
        # get div
        div = score.find('div', class_='col-xs-12 col-sm-5 subject')
        if div is None:
            continue
        
        # get subject name
        sub = div.text
        
        # skip the title row
        if sub == 'Subject':
            continue
        
        # get score for subjects that we care for
        if sub in ['Science', 'Math', 'English']:
            school[sub] = score.find('div', class_='score').text
    
    return school


# read school list
with open('data/school_links.txt', 'r') as f:
    school_links = f.read().split('\n')

# define keys for csv file
keys = ['Name', 'Address', 'Zipcode', 'Science', 'Math', 'English', 'College', 'Progress']
    
# dump as csv file
f = open('data/school_performance.csv', 'w', 0)
f.write("'" + ("','").join(keys) + "'")

# loop over all schools
for school_link in school_links:
    print('Link: ' + school_link)
    
    school = parse_school_page(school_link)
    print school
    
    row = []
    for k in keys:
        if k in school:
            row.append(school[k])
        else:
            row.append('')
    
    f.write("\n'" + ("','").join(row) + "'")
    time.sleep(1)
    
f.close()





