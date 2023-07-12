#Step 1. 필요한 모듈을 로딩합니다.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request,time,os

def ts(x) :
    time.sleep(x)

#Step 2. 사용자에게 필요한 정보를 입력 받습니다.
query_txt = input('1.크롤링할 이미지의 키워드?: ')
cnt = int(input('2.크롤링 할 건수는?: '))

# 파일만들기
now = f"c:/py_temp/{query_txt}.txt"
os.makedirs(now)
os.chdir(now)

# Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
driver = webdriver.Chrome()
base_link = 'https://search.naver.com/search.naver?where=view&sm=tab_jum&query='
driver.get(base_link + query_txt)
driver.find_element(By.XPATH, '//*[@id="snb"]/div[1]/div/div[1]/a[2]').click()

# 웹페이지를 6회 스크롤 다운 합니다 (END 키 전송)
for i in range(1) :
    time.sleep(3)
    driver.find_element(By.XPATH,'//body').send_keys(Keys.END)

from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

a_href = [ ]
for i in soup.find_all('a',class_='api_txt_lines total_tit') :
    a_href.append(i["href"])
for idx, save_title in enumerate(a_href, start = 1) :
    urllib.request.urlretrieve(save_title, str(idx) + ".txt")
    if idx == cnt :
        break

driver.close()