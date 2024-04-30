import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import getpass as gp
from datetime import datetime, timedelta, timezone
import sys

accounts = ['Mr_Derivatives',
          'warrior_0719',
          'ChartingProdigy',
          'allstarcharts',
          'yuriymatso',
          'TriggerTrades',
          'AdamMancini4', 
          'CordovaTrades', 
          'Barchart']

timeSlot=300 #converted to 5 minutes (time interval of scraping)
word = "$SPX"

def setUpDriver(account,cashedWord):
    webdriver_url = 'http://localhost:9515'
    options = webdriver.ChromeOptions()
    options.headless = True
    options.add_argument("start-maximized")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36')
    driver = webdriver.Remote(command_executor=webdriver_url, options=options)
    driver.get('https://twitter.com/login')
    time.sleep(7)
    username=driver.find_element(By.XPATH,"//input[@name='text']")
    username.send_keys('GeeksTest231')
    next=driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
    next.click()
    time.sleep(7)
    password= driver.find_element(By.XPATH,"//input[@name='password']")
    password.send_keys('GeeksForGeeks')
    login=driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
    login.click()
    time.sleep(10)
    search=driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
    search.send_keys(account)
    search.send_keys(Keys.ENTER)
    time.sleep(5)
    people=driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
    people.click()
    time.sleep(5)
    profile=driver.find_element(By.XPATH,"//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]"
)
    profile.click()
    time.sleep(7)
    Tweets=driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    tweet_texts=[]
    tweet_times=[]
    loop_count_break=0
    currentDate = datetime.now(timezone.utc)
    for tweet in Tweets:
        withinRange=True
        tweetTime= tweet.find_element(By.XPATH,".//time").get_attribute('datetime')
        tweetTimeCheck= datetime.fromisoformat(tweetTime)
        if(currentDate-tweetTimeCheck>timedelta(hours=2)):
                loop_count_break+=1
                withinRange=False
        time.sleep(5)
        
        if(withinRange and tweet.find_element(By.XPATH,".//div[@data-testid='tweetText']")!=None):
                tweetText= tweet.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
                tweet_texts.append(tweetText)
                tweet_times.append(tweetTime)
                time.sleep(3)    
        
        if(loop_count_break>3):
            break
    driver.quit()    
    return count(tweet_texts,tweet_times,cashedWord)


def count(texts,tweet_times,cashedWord):
    counterTime=0
    countWordMention=0
    currentDate = datetime.now(timezone.utc)
    for text in texts:
        tweetTime= datetime.fromisoformat(tweet_times[counterTime])
        if(cashedWord in text):
            if(currentDate-tweetTime<=timedelta(hours=2)):
                countWordMention+=1
        counterTime+=1        
    return countWordMention

def retrieveAll(accounts,word):
    counterAll=0
    for account in accounts:
        countAccount=0
        countAccount=setUpDriver(account,word)
        counterAll+=countAccount
        print("Number of times "+word +" mentioned within time range in account of "+ account, ": ",countAccount)
        time.sleep(5)
    return counterAll   

def scriptTwitterScrap(accounts,timeSlot,cashTagWord):
    while(True):
        time2=timeSlot/60
        result=retrieveAll(accounts,cashTagWord)
        print(cashTagWord+ " was mentioned a total of: ",result, " times in the last 2 hours!")
        time.sleep(timeSlot)
        print(time2, " minutes passed --> Check Results Now:")

                
scriptTwitterScrap(accounts,timeSlot,word)