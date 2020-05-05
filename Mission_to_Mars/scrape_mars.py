from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import time
import requests
import re

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'}
    return Browser('chrome', **executable_path, headless=False)
    


def scrape():
    browser = init_browser()
    scrapped_data = {}

    #Scrapping the NASA news
    url_news="https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    browser.visit(url_news)
    time.sleep(10)
    html=browser.html
    soup=bs(html,"html.parser")
    time.sleep(5)
    titles=soup.find_all("div",class_="content_title")
    # print(titles[1])
    news_title=titles[1].text
    # print(f"Latest news: {news_title}")

    #Scrapping the news para

    
    browser.click_link_by_text(news_title)
    time.sleep(10)
    html=browser.html
    soup=bs(html,"html.parser")
    para=soup.find("i")
    news_p=para.text
    #print(f"Latest news para: {news_p}")

    #Scrapping the featured image
    url_image="https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(url_image)
    time.sleep(5)
    browser.click_link_by_partial_text('FULL IMAGE')
    time.sleep(5)
    browser.click_link_by_partial_text('more info')
    time.sleep(5)
    html=browser.html
    
    soup=bs(html,"html.parser")

    image_url=soup.find("figure",class_="lede").find("a")
    # print(image_url)
    image_url["href"]
    featured_image_url="https://www.jpl.nasa.gov"+image_url["href"]
    # print(featured_image_url)

    #Scrapping the weather tweet
    url_tweet="https://twitter.com/marswxreport?lang=en"
    
    page = requests.get(url_tweet)
    time.sleep(10)
    soup = bs(page.text, "html.parser")
    
    
   
    weather_tweets = soup.find_all("div",class_="js-tweet-text-container")
     #Finding weather tweets
    filtered_weather_tweets=[]

    for tweet in weather_tweets:
        if "low" in tweet.p.text and "high" in tweet.p.text and "winds" in tweet.p.text and "pressure" in tweet.p.text:
            filtered_weather_tweets.append(tweet.p.text)

    weather_tweet=filtered_weather_tweets[0]
    trimmmed_tweet=re.split("pic.twitter.com",weather_tweet,1)
    weather_tweet=trimmmed_tweet[0]
    trimmmed_tweet=re.split("InSight",weather_tweet,1)
    weather_tweet=trimmmed_tweet[1]
    weather_tweet=weather_tweet.strip()
    weather_tweet=weather_tweet.replace("sol","Sol")
    
    #Scrapping the fact table
    url_fact="https://space-facts.com/mars/"
    tables = pd.read_html(url_fact)
    #tables
    fact_table=tables[0]
    fact_table.rename(columns={0:"description", 1:"value"},inplace= True)
    fact_table.set_index("description", inplace=True)
    mars_fact=fact_table.to_html(index=True,justify="left")
    

    #Scrapping the hemisphere image url
    url_hem="https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
    browser.visit(url_hem)
    time.sleep(5)
    html=browser.html
    soup=bs(html,"html.parser")
    names=soup.find_all("div",class_="description")

    titles=[]
    for n in names:
        titles.append(n.a.h3.text)
    # print(titles)    

    hemisphere_image_urls=[]
    for title in titles:
        browser.click_link_by_partial_text(title)
        time.sleep(5)
        html=browser.html
        soup=bs(html,"html.parser")
        im_url=soup.find("div",class_="downloads").li.a["href"]
        hemisphere_image_urls.append({"title":title,"img_url":im_url})
        browser.back()    
    
    scrapped_data["news_title"]=news_title
    scrapped_data["news_para"]=news_p
    scrapped_data["featured_image_url"]=featured_image_url
    scrapped_data["weather_tweet"]=weather_tweet
    scrapped_data["fact_table"]=mars_fact
    scrapped_data["hemisphere_url"]=hemisphere_image_urls

    return scrapped_data

    
#dict=scrape()
#print(dict)