# riss.com 사이로 제어 및 데이터 수집하기
from selenium import webdriver
import time, os, sys
driver = webdriver.Chrome()


# 웹사이트 접속하기
driver.get('https://www.riss.kr')
time.sleep(2)
driver.maximize_window()  # 반응형 웹사이트의 경우 화면창에 따라 버튼이 달라질수 있어서 창의 크기를 맞춰두고 시작

# 사이트 팝업창 닫기
from selenium.webdriver.common.by import By

main = driver.window_handles
for i in main:
    if i != main[0]:
        driver.switch_to.window(i)
        time.sleep(2)
        driver.close()

driver.switch_to.window(main[0])

# 검색창에 검색어 넣기
driver.find_element(By.ID, 'query').send_keys('여름여행'+'\n')
time.sleep(2)
driver.find_element(By.LINK_TEXT, '국내학술논문').click()
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="tabMenu"]/ul/li/div/ul/li[3]/a/span').click()


# 웹사이트 닫기
time.sleep(5)
driver.close()













