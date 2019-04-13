from selenium import webdriver

url = "https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL"

browser = webdriver.PhantomJS(executable_path = '/usr/local/bin/PhantomJS')
browser.get(url)
print(browser.page_source)
browser.quit()
