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


    hemi = []

    for i in range(4):
    html = browser.html
    soup = bs(html, 'html.parser')

    title = soup.find_all('h3')[i].get_text()
    browser.find_by_tag('h3')[i].click()
    
    html = browser.html
    soup = bs(html, 'html.parser')
    
    hemi_img = soup.find('a', text='Sample')['href']
    browser.back()


    hemi.append({
        'title':title,
        'hemi_img': hemi_img
    })



    mars_data = {
    "news_title": news_title,
    "news_p": news_p,
    'featured_image_url': featured_image_url,
    'hemi_scrape': hemi
    }
    return mars_data
    