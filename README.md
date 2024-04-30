# TwitterScrapping
Python code used for scrapping data from Twitter accounts.

# Dependencies & Libraries
1- Install Selenium: pip install selenium
2- Download Edge/Chrome webdriver & replace its local url in the python code 

# Some Notes:
1- Using requests.get wouldn't work because it fetches static pages mainly, and it wouldn't fetch the entire html pages. 
2- I suffered with Selenium. It was working well at first using BeautifulSoup applied after using driver.get() to fetch the page sources, but then I ran into the issue that that my webdriver opens the twitter accounts older versions (not up to date), so I couldn't manipulate the html for accurate results. It is important to note that this is the reason why I choose to login first with a fake account.
3- After watching multiple youtube videos (BeautifulSoup on freecodecamp, how to use selenium with web browsers and even scrapy), this is the best I've come so far. 
