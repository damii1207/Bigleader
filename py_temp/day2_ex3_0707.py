#Step 1. 필요한 모듈을 로딩합니다.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import urllib.request,time,os

#Step 2. 사용자에게 필요한 정보를 입력 받습니다.
query_txt = input('1.크롤링할 이미지의 키워드?: ')
cnt = int(input('2.크롤링 할 건수는?: '))

# 현재시간 활용 폴더 생성
now = "c:/py_temp/" + time.strftime("%Y%m%d_%H%M%S") +'-' + query_txt
os.makedirs(now)
os.chdir(now)

# Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
driver = webdriver.Chrome()
base_link = 'https://search.naver.com/search.naver?''where=image&sm=tab_jum&query='
driver.get(base_link + query_txt)

# 웹페이지를 6회 스크롤 다운 합니다 (END 키 전송)
for i in range(6) :
    time.sleep(3)
    driver.find_element(By.XPATH,'//body').send_keys(Keys.END)

# Step 4. 이미지 추출하기
soup = BeautifulSoup(driver.page_source, 'html.parser')
img_src = [ ]

for i in soup.find_all('img', class_ = '_image _listImage') :
    img_src.append(i["src"])
for idx, save_img in enumerate(img_src, start = 1) :
    urllib.request.urlretrieve(save_img, str(idx) + ".jpg")
    if idx == cnt :
        break
driver.close()
