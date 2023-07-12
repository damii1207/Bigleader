# 웹사이트 오픈하고 닫기
from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os, sys
def ts(x) :
    time.sleep(x)
driver = webdriver.Chrome()
driver.get('https://www.riss.kr')

# 팝업창이 있으면 닫고 창 최대화 하기
all_win = driver.window_handles
for handle in all_win :
    if handle != all_win[0] :
        driver.switch_to.window(handle)
        ts(1); driver.close()
driver.switch_to.window(driver.window_handles[0])
ts(2); driver.maximize_window()

# 검색창 클릭하고 엔터 입력하기
ts(2); driver.find_element(By.ID, 'query').send_keys('빅데이터')
ts(2); driver.find_element(By.CLASS_NAME, 'btnSearch').click()

# 원하는 버튼 클릭하기
ts(2); driver.find_element(By.LINK_TEXT, '학위논문').click()
from bs4 import BeautifulSoup
soup = BeautifulSoup(driver.page_source, 'html.parser')

# 게시물 제목만 추출하기
논문 = soup.find('div', class_='srchResultListW')
제목 = 논문.find_all('p', class_='title')
저자 = 논문.find_all('span', class_='writer')
소속 = 논문.find_all('span', class_='assigned')

import sys
원본 = sys.stdout
with open('c:/py_temp/riss.txt','a') as 파일 :
    ## 'a' => 'append' , 'w' => write
    sys.stdout = 파일

    for i in 제목 :
        print(i.get_text())
sys.stdout = 원본

for i in 소속 :
    print(i.get_text())

# 창 닫기
ts(5); driver.close()















