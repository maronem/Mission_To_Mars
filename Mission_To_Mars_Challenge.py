
# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

# Set executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# ### NASA Mars Webscraping

# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

#setup html parser

html = browser.html
news_soup = soup(html, 'html.parser')

# This variable holds all the information from 'div'
slide_elem = news_soup.select_one('div.list_text')

# Scrape the title of the latest article
# we chained .find onto our previously assigned variable, slide_elem.

slide_elem.find('div', class_='content_title')


# Use select out title text from html compnents

news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text

news_text = slide_elem.find('div', class_='article_teaser_body').get_text()
news_text



# ### JPL Image Scraping


# Visit the JPL image webpage
url = 'https://spaceimages-mars.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Find and click the full image button

full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse resulting image html with soup

html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url

img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# Add base URL to create an absolute URL

img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url



#### Mars Fact Table Scraping


# Visit the JPL image webpage
url = 'https://galaxyfacts-mars.com/'
browser.visit(url)

# Scrape entire table with Pandas
# read_html() = searches and returns a list of tables found in the HTML

df = pd.read_html('https://galaxyfacts-mars.com/')[0]
df.columns = ['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


# Convert DF back to HTML ready code

df.to_html()

browser.quit()


# # Mission To Mars Challege Code

# Import Splinter, BeautifulSoup, and Pandas
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd


# Set the executable path and initialize Splinter
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


### Visit the NASA Mars News Site

# Visit the mars nasa news site
url = 'https://redplanetscience.com/'
browser.visit(url)

# Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)

# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')

slide_elem = news_soup.select_one('div.list_text')
slide_elem.find('div', class_='content_title')

# Use the parent element to find the first a tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title

# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


### JPL Space Images Featured Image

# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)

# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()

# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')
img_soup

# find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel

# Use the base url to create an absolute url
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url


### Mars Facts
df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.head()
df.columns=['Description', 'Mars', 'Earth']
df.set_index('Description', inplace=True)
df
df.to_html()

# Quit Browser
browser.quit()



# D1: Scrape High-Resolution Mars’ Hemisphere Images and Titles

### Hemispheres

# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'
browser.visit(url)

# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.

for img in range(4):
    
    # Create empty dictionary
    hemispheres = {}
    
    # Click full-res image link
    browser.find_by_css('a.product-item h3')[img].click()
    
    # Get URL string and full-rest image URL
    element = browser.links.find_by_text('Sample').first
    img_url = element['href']
    title = browser.find_by_css("h2.title").text
    
    # Save values into variables
    hemispheres["img_url"] = img_url
    hemispheres["title"] = title
    
    # Append values to dictionary
    hemisphere_image_urls.append(hemispheres)
    browser.back()

# Quit the browser
browser.quit()

# Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls





