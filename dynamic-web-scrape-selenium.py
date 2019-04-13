from selenium import webdriver

url = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"

browser = webdriver.Firefox()
browser.get(url)
browser.quit()