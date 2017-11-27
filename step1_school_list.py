import time
import requests
from bs4 import BeautifulSoup as bs

# below is the search link without specifying a page number
url = 'https://www.greatschools.org/search/search.page?gradeLevels=h&q=high+school&st%5B%5D=public&st%5B%5D=charter&page='

# get the max page number
html_doc = requests.get(url + "1")
soup = bs(html_doc.text, 'html.parser')
last_page = soup.find_all('li', class_='page')[-1].find('a').text
print("Maximum page numbers = %s" % (last_page))

# prepare the loop over all pages
pages = range(637, int(last_page) + 1)
school_links = []

# loop over all pages and find out all links
for page in pages:
    
    print("-> Get page %d/%s" % (page, last_page))
    html_doc = requests.get(url + str(page))
    soup = bs(html_doc.text.encode("ascii","ignore"), 'html.parser')
    
    # find all links with specific classes
    links = soup.find_all('a', class_='open-sans_sb mbs font-size-medium rs-schoolName')

    for link in links:
        print("  -> School Name: %-30s   link=%s" % (link.text, link["href"]))
        school_links.append(link["href"])
    
    # sleep 1 seconds to prevent blocking by the website
    time.sleep(1)
    
# dump out the result

with open('data/school_links.txt', 'w') as f:
    f.write(("\n").join(school_links))