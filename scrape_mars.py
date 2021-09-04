from splinter import Browser, browser
from bs4 import BeautifulSoup as bs
import time
from webdriver_manager.chrome import ChromeDriverManager


def scrape_info():
    # Set up Splinter
    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)

    # Visit visitcostarica.herokuapp.com
    url = "https://redplanetscience.com/"
    browser.visit(url)

    time.sleep(1)

    # Scrape page into Soup
    html = browser.html
    soup = bs(html, "html.parser")

# Parse HTML with Beautiful Soup
    soup = bs(html, 'html.parser')
    news_title = soup.find('div', class_='content_title').text
    news_p = soup.find('div', class_= 'article_teaser_body').text
    # Store data in a dictionary
    browser.quit()

    executable_path = {'executable_path': ChromeDriverManager().install()}
    browser = Browser('chrome', **executable_path, headless=False)


    url = 'https://spaceimages-mars.com/'
    browser.visit(url)

    time.sleep(1)

    full_image = soup.find_all('a', class_= 'showimg fancybox-thumbs')['href']
    featured_image_url = url + full_image
    # Close the browser after scraping
    browser.quit()


    mars_data = {
    "news_title": news_title,
    "news_p": news_p,
    'featured_image_url': featured_image_url
    }
    return mars_data
    