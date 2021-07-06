import pandas as pd

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup
import time
import pandas as pd
from selenium.webdriver.support.ui import Select
from html_table_parser import parser_functions as parser

chromedriver_autoinstaller

# 다나와 사이트 검색
options = Options()
options.add_argument('headless'); # headless는 화면이나 페이지 이동을 표시하지 않고 동작하는 모드

# webdirver 설정(Chrome, Firefox 등)
chromedriver_autoinstaller.install()
# driver = webdriver.Chrome(options=options) # 브라우저 창 안보이기
driver = webdriver.Chrome() # 브라우저 창 보이기

# 크롬 브라우저 내부 대기 (암묵적 대기)
driver.implicitly_wait(5)

# 브라우저 사이즈
driver.set_window_size(1920, 1280)

# 페이지 이동(다나와 유럽 URL)
url = 'http://auto.danawa.com/newcar/?Work=record&Tab=Top10&Brand=303&Month=2017-01-00&MonthTo=2018-01-00'

# driver = Chrome()
driver.get(url)

#bs4 초기화
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 2017~2018
temp = soup.find_all('table')
temp

p = parser.make2d(temp[0])

p#ndarray

df = pd.DataFrame(p[2:], columns=p[0])
print(df)