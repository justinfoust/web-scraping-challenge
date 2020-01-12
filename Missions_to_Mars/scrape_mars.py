###---------------------------------------------------------###
###   Web Scraping HW -- Mission to Mars                    ###
###   Justin Foust  --  01/11/2020  --  Data Boot Camp      ###
###---------------------------------------------------------###


from bs4 import BeautifulSoup as bs
from splinter import Browser
import pandas as pd
import time

def scrape():
    browser = Browser('chrome')
    scrapings = {}

    #NASA Mars News
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    results = soup.find_all('li', class_='slide')
    scrapings['news_results'] = {
        'news_title': results[0].find('div', class_='content_title').a.text,
        'news_p': results[0].find('div', class_='article_teaser_body').text
    }


    # #JPL Mars Space Images
    url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url)

    xpath = '//li[@class="slide"]'

    results = browser.find_by_xpath(xpath)
    img = results[0]
    img.click()

    time.sleep(3)

    html = browser.html
    soup = bs(html, 'html.parser')
    scrapings['img_url'] = "https://www.jpl.nasa.gov" + soup.find('img', class_='fancybox-image')['src']


    # #Mars Weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)

    time.sleep(5)

    html = browser.html
    soup = bs(html, 'html.parser')
    scrapings['mars_weather'] = soup.find('div', class_='js-tweet-text-container').p.contents[0]


    # #Mars Facts
    url = 'https://space-facts.com/mars/'
    tables = pd.read_html(url)
    clean = tables[0].set_index(0).rename(columns={1:''}).rename_axis(index={0: ''})
    scrapings['table_string'] = clean.to_html(classes='table')


    # #Mars Hemispheres
    url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    hemisphere_image_urls = []

    xpath = '//div[@class="item"]/a/img'

    browser.visit(url)
    results = browser.find_by_xpath(xpath)

    for i in range(len(results)):
        browser.visit(url)
        result = browser.find_by_xpath(xpath)
        result[i].click()
        
        time.sleep(3)

        html = browser.html
        soup = bs(html, 'html.parser')
        hemisphere_image_urls.append({
            'title': soup.find('h2', class_='title').text,
            'img_url': soup.find('div', class_='downloads').find('a', text='Sample')['href']
        })
    
    scrapings['hemisphere_image_urls'] = hemisphere_image_urls

    browser.quit()

    return scrapings

# scrape()