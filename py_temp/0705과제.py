# riss.com 사이로 제어 및 데이터 수집하기
from selenium import webdriver
import time, os, sys
driver = webdriver.Chrome()

# 웹사이트 접속하기
from selenium.webdriver.common.by import By
driver.get('https://korean.visitkorea.or.kr/main/main.do')
driver.set_window_size(1200,700) # 반응형 웹사이트의 경우 화면창에 따라 버튼이 달라질수 있어서 창의 크기를 맞춰두고 시작
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="placeHolder"]/a').click()
time.sleep(1)
driver.find_element(By.ID, 'inp_search').send_keys('여름여행'+'\n')
time.sleep(2)
driver.find_element(By.XPATH, '//*[@id="sorting_options"]/button[4]/span').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="32"]/button/span').click()

# 웹사이트 닫기
time.sleep(5)
driver.close()