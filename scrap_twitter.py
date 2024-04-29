from bs4 import BeautifulSoup
import os
from datetime import datetime
from selenium import webdriver
import requests
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



def retrieveHtmlPages(account):
    webdriver_url = 'http://localhost:9515'
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=webdriver_url, options=options)
    driver.get(account) 
    wait = WebDriverWait(driver, 30)
    html_text = driver.page_source
    soup = BeautifulSoup(html_text, "lxml")
    main=(soup.find('div', attrs={'data-testid': 'primaryColumn'})).prettify()
    driver.quit()
    return main

def retrieve(account):
    webdriver_url = 'http://localhost:9515'
    options = webdriver.ChromeOptions()
    driver = webdriver.Remote(command_executor=webdriver_url, options=options)
    driver.get(account) 
    
    # Wait for the posts to finish loading
    wait = WebDriverWait(driver, 30)
    posts_loaded = wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'article[data-testid="tweet"]')))
    
    # Once the posts are loaded, fetch the page source
    html_text = driver.page_source
    
    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(html_text, "lxml")
    
    # Find the main content (if needed)
    main_content = soup.find('div', attrs={'data-testid': 'primaryColumn'}).prettify()
    
    # Quit the driver
    driver.quit()
    
    return main_content


account1= retrieve('https://twitter.com/Mr_Derivatives')
#account2=retrieveHtmlPages('https://twitter.com/warrior_0719')
#account3=retrieveHtmlPages('https://twitter.com/ChartingProdigy')
#account4=retrieveHtmlPages('https://twitter.com/allstarcharts')
#account5=retrieveHtmlPages('https://twitter.com/yuriymatso')
#account6=retrieveHtmlPages('https://twitter.com/TriggerTrades')
print(account1)