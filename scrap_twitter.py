from bs4 import BeautifulSoup
import os
from datetime import datetime
from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import urllib.request 

def retrieve(account):
    webdriver_url = 'http://localhost:9515'
    options = webdriver.ChromeOptions()
    service = webdriver.ChromeService(service_args=['--disable-build-check'])
    options.page_load_strategy = 'normal'
    driver = webdriver.Remote(command_executor=webdriver_url, options=options)
    driver.get(account) 
    wait = WebDriverWait(driver,200)
    time_loaded = wait.until(EC.presence_of_all_elements_located((By.TAG_NAME, 'time')))
    a_tag=wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'a[dir="ltr"]')))
    conditions = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'div[data-testid="tweetText"]')))
    article_loaded = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, 'article[data-testid="tweet"]')))
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, "lxml")
    main_content=soup.find('div',attrs={'data-testid': 'primaryColumn'})
    tweets = soup.find_all('div',attrs={'data-testid': 'tweetText'})
  #  driver.quit()
    return tweets

    try: 
        
        response =  urllib.request.urlopen(account)
        data = response.read() 
        html_content = data.decode('utf-8') 
        print(html_content) 
  
    except Exception as e:
         print("Error fetching URL:", e) 



def retrieveMentions(account,cashtag):
    tweets=retrieve(account)
    mentioned_count = 0
    current_time = datetime.now()
    for tweet in tweets:
        a_tags=tweet.find_all('a')
        for a_tag in a_tags:
            if cashtag in a_tag.text:
                tweet_timeTag = a_tag.find('time')
                if tweet_timeTag:
                   tweet_time = tweet_timeTag.get('datetime')
                   if tweet_time:
                      tweet_time = datetime.strptime(tweet_time, '%Y-%m-%dT%H:%M:%S.%fZ')
                      difference = current_time - tweet_time
                      if difference <= 3600*24*30:
                          mentioned_count += 1
                          break 
    return mentioned_count
account1= retrieve('https://twitter.com/Mr_Derivatives')
#account2= retrieveMentions('https://twitter.com/warrior_0719',"$TSLA")
#account3= retrieve('https://twitter.com/ChartingProdigy')
#=account4=retrieveHtmlPages('https://twitter.com/allstarcharts')
#account5=retrieveHtmlPages('https://twitter.com/yuriymatso')
#account6=retrieveHtmlPages('https://twitter.com/TriggerTrades')
print(len(account1))
