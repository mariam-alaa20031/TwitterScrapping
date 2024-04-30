import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import getpass as gp
from datetime import datetime, timedelta, timezone


accounts=['Mr_Derivatives',
          'warrior_0719',
          'ChartingProdigy',
          'allstarcharts',
          'yuriymatso',
          'TriggerTrades',
          'AdamMancini4', 
          'CordovaTrades', 
          'Barchart'
]

account_XPATH="//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[3]/section/div/div/div[1]/div/div/div/div/div[2]/div[1]/div[1]/div/div[1]/a/div/div[1]/span/span[1]"

def setUpDriver(account,account_Xpath,cashedWord):
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
    time.sleep(10)
    username=driver.find_element(By.XPATH,"//input[@name='text']")
    username.send_keys('GeeksTest231')
    next=driver.find_element(By.XPATH,"//span[contains(text(),'Next')]")
    next.click()
    time.sleep(10)
    password= driver.find_element(By.XPATH,"//input[@name='password']")
    password.send_keys('GeeksForGeeks')
    login=driver.find_element(By.XPATH,"//span[contains(text(),'Log in')]")
    login.click()
    time.sleep(10)
    search=driver.find_element(By.XPATH,"//input[@data-testid='SearchBox_Search_Input']")
    search.send_keys(account)
    search.send_keys(Keys.ENTER)
    time.sleep(10)
    people=driver.find_element(By.XPATH, "//span[contains(text(),'People')]")
    people.click()
    time.sleep(10)
    profile=driver.find_element(By.XPATH,account_Xpath)
    profile.click()
    time.sleep(10)
    Tweets=driver.find_elements(By.XPATH,"//article[@data-testid='tweet']")
    tweet_texts=[]
    tweet_times=[]
    currentDate = datetime.now(timezone.utc)
    for tweet in Tweets:
        tweetTime= datetime.fromisoformat(tweet.find_element(By.XPATH,".//time").get_attribute('datetime'))
        time.sleep(10)
        if(currentDate-tweetTime>timedelta(minutes=60)):
            break
        tweetText= tweet.find_element(By.XPATH,".//div[@data-testid='tweetText']").text
        time.sleep(10)
        tweet_texts.append(tweetText)
        tweet_times.append(tweetTime)
        print(tweetText)
        print(tweet_times)
    return count(tweet_texts,cashedWord)


def count(texts,cashedWord):
    counterTime=0
    countWordMention=0
    for text in texts:
        if(cashedWord in text):
            print("In HERE!")
            countWordMention+=1
        counterTime+=1        
    return countWordMention

def retrieveAll(accounts,accountsPath,word):
    counterAll=0
    for account in accounts:
        counterAll+=setUpDriver(account,accountsPath,word)
        print("Word count after ", account , " was ",counterAll)
    return word +" was mentioned ",counterAll, "in the last 40 minutes!"    


retrieveAll(accounts,account_XPATH,"$SPY")
                
