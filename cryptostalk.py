from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import time

try:
    opts = Options()
    opts.headless = True
    browser = Firefox()
    url = 'http://cryptocurrencyprices.stockmaster.in/cryptocurrency-prices-in-inr-india/'
    browser.get(url)
    prices = []

    for i in range(1,25):
        price = browser.find_element_by_xpath(f'/html/body/div[6]/div[2]/div/div/section[3]/div/div/div[1]/div/div/div/div/div/div/div[4]/table/tbody/tr[{i}]/td[3]').text
        prices.append(price)

    short_names = []

    for i in range(1,25):
        sn = browser.find_element_by_xpath(f'/html/body/div[6]/div[2]/div/div/section[3]/div/div/div[1]/div/div/div/div/div/div/div[4]/table/tbody/tr[{i}]/td[2]/div/a/span[2]').text
        short_names.append(sn)
    
    names = []

    for i in range(1,25):
        name = browser.find_element_by_xpath(f'/html/body/div[6]/div[2]/div/div/section[3]/div/div/div[1]/div/div/div/div/div/div/div[4]/table/tbody/tr[{i}]/td[2]/div/a/span[3]').text
        names.append(name)

    cryptocurrency = zip(names,short_names,prices)
    for i,j,k in cryptocurrency:
        print(i,j,k)


    browser.close()
except:
    browser.close()