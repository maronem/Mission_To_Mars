# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import requests
import pandas as pd

# Create executable path
executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


### NASA Mars Webscraping


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


### JPL Image Scraping


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


### Mars Fact Table Scraping


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


# Quit automated browser
browser.quit()
