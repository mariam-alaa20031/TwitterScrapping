from bs4 import BeautifulSoup
import os
from datetime import datetime
from selenium import webdriver


def retrieveHtmlPages(account):
    webdriver_url = 'http://localhost:9515'
    options = webdriver.EdgeOptions()
    driver = webdriver.Remote(command_executor=webdriver_url, options=options)
    driver.get(account)
    driver.implicitly_wait(10)
    html_text = driver.page_source
    return html_text

account1=retrieveHtmlPages('https://twitter.com/Mr_Derivatives')
account2=retrieveHtmlPages('https://twitter.com/warrior_0719')
account3=retrieveHtmlPages('https://twitter.com/ChartingProdigy')
account4=retrieveHtmlPages('https://twitter.com/allstarcharts')
account5=retrieveHtmlPages('https://twitter.com/yuriymatso')
account6=retrieveHtmlPages('https://twitter.com/TriggerTrades')
