import chromedriver_autoinstaller
chromedriver_autoinstaller.install()
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

co = Options()
co.add_experimental_option('debuggerAddress', '127.0.0.1:9222')
driver = webdriver.Chrome(options=co)


brands = [303,304,307,312,316,326,321,322,337,329,328,349,371,376,413,422,618,367,459,394,399,381,440,436,445,404,408,409,390,385,622, 491,486,500,537,617]
for brand in brands[:1]:
    url = f'http://auto.danawa.com/newcar/?Work=record&Tab=Top10&Month=2021-06-00&MonthTo=2021-06-00&Brand={brand}'
    url = 'http://auto.danawa.com/newcar/?Work=record&Tab=Top10&Brand=303&Month=2017-01-00&MonthTo=2018-01-00'
    time.sleep(2)
    driver.get(url)
    with open(f'./crawl_result/{brand}.html', 'w+', encoding='utf-8') as f:
        f.write(driver.page_source)




