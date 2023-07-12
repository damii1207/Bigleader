# Chap 15.riss.kr 에서 특정 키워드로 논문 / 학술 자료 검색하기

# Step 1. 필요한 모듈을 로딩합니다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.chrome.service import Service
import time

# Step 2. 사용자에게 검색 관련 정보들을 입력 받습니다.
query_txt = '빅데이터'

# Step 3. 수집된 데이터를 저장할 파일 이름 입력받기
f_dir = input("2.파일을 저장할 폴더명만 쓰세요(기본값:c:\\py_temp\\):")
if f_dir == '':
    f_dir = "c:\\py_temp\\"

# Step 4. 크롬 드라이버 설정 및 웹 페이지 열기
driver = webdriver.Chrome()
url = 'http://www.riss.kr/'
driver.get(url)
driver.maximize_window()
time.sleep(2)

# Step 5. 자동으로 검색어 입력 후 조회하기
driver.find_element(By.ID, 'query').send_keys(query_txt + '\n')

# Step 6.학위 논문 선택하기
driver.find_element(By.LINK_TEXT, '학위논문').click()
time.sleep(2)

# Step 7.Beautiful Soup 로 본문 내용만 추출하기
from bs4 import BeautifulSoup

soup_1 = BeautifulSoup(driver.page_source, 'html.parser')

# Step 8. 총 검색 건수를 보여주고 수집할 건수 입력받기
import math

total_cnt = soup_1.find('div', 'searchBox pd').find('span', 'num').get_text()
print('검색하신 키워드 %s (으)로 총 %s 건의 학위논문이 검색되었습니다' % (query_txt, total_cnt))
cnt = 15
page_cnt = math.ceil(cnt / 10)
print('%s 건의 데이터를 수집하기 위해 %s 페이지의 게시물을 조회합니다.' % (cnt, page_cnt))
print("\n")

# Step 9. 데이터 수집하기
no2 = []  # 게시글 번호 컬럼
title2 = []  # 게시글 제목 컬럼
author2 = []  # 논문 저자 컬럼
company2 = []  # 소속 기관 컬럼
date2 = []  # 게시글 날짜 컬럼
suksa2 = []  # 국내석사 컬럼
contents2 = []  # 초록내용
full_url2 = []  # 논문 원본 URL

no = 1  # 게시글 번호 초기값

for a in range(1, page_cnt + 1):
    print("\n")
    print("%s 페이지 내용 수집 시작합니다 =======================" % a)

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    content_list = soup.find('div', 'srchResultListW').find_all('li')

    for i in content_list:
        # 논문 제목 체크하기
        try:
            title = i.find('p', 'title').get_text().strip()
        except:
            continue
        else:
            # 1.게시글 번호
            print("\n")
            print("%s 번째 정보를 추출하고 있습니다============" % no)
            no2.append(no)
            print("1.번호 : %s" % no)

            # 2. 논문 제목
            title2.append(title.strip())
            print("2.제목 : %s" % title.strip())

            # 3. 작성자
            try:
                author = i.find('p', 'etc').find('span', 'writer').get_text().strip()
            except:
                author = '작성자가 없습니다'
                print("3.작성자 : %s" % author.strip())
                author2.append(author.strip())
            else:
                author2.append(author.strip())
                print("3.작성자 : %s" % author.strip())

            # 4. 소속기관
            try:
                company = i.find('p', 'etc').find('span', 'assigned').get_text().strip()
            except:
                company = '소속 기관이 없습니다'
                company2.append(company.strip())
                print("4.소속기관 : %s" % company.strip())
            else:
                company2.append(company.strip())
                print("4.소속기관 : %s" % company.strip())

            # 5. 발표날짜
            try:
                date_1 = i.find('p', 'etc').find_all('span')
                date_2 = date_1[2].get_text().strip()
            except:
                date_2 = '발표날짜가 없습니다'
                date2.append(date_2)
                print("5.발표년도 : %s" % date_2)
            else:
                date2.append(date_2)
                print("5.발표년도 : %s" % date_2)

            # 6.학위여부
            try:
                suksa_1 = i.find('p', 'etc').find_all('span')
                suksa_2 = suksa_1[3].get_text().strip()
            except:
                suksa_2 = '학위가 없습니다'
                suksa2.append(suksa_2)
                print("6.학위여부 : %s" % suksa_2)
            else:
                suksa2.append(suksa_2)
                print("6.학위여부 : %s" % suksa_2)

            # 7.초록 내용-해당 논문의 상세 내역에서 추출할 수 있음.
            url_1 = i.find('p', 'title').find('a')['href']
            full_url = 'http://www.riss.kr' + url_1
            time.sleep(1)
            driver.get(full_url)

            soup_1 = BeautifulSoup(driver.page_source, 'html.parser')
            try:
                cont = soup_1.find("div", "text").find('p').get_text().replace("\n", "").strip()
            except:
                cont = '초록이 없습니다'
                contents2.append(cont)
                print("7.초록내용 : %s" % cont)
            else:
                contents2.append(cont)
                print("7.초록내용 : %s" % cont)

            time.sleep(1)

            # 8.논문 url 주소
            full_url2.append(full_url)
            print('8.논문 URL 주소:', full_url)

            driver.back()  # 이전 페이지로 돌아가기

            time.sleep(2)

            no += 1

            if no > cnt:
                break

    a += 1
    b = str(a)

    try:
        driver.find_element(By.LINK_TEXT, '%s' % b).click()
    except:
        driver.find_element(By.LINK_TEXT, '다음 페이지로').click()

print("요청하신 작업이 모두 완료되었습니다")

# Step 10. 수집된 데이터를 xls와 csv 형태로 저장하기
# 현재 날짜와 시간으로 폴더 만들고 파일 이름 설정하기
import os

n = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (n.tm_year, n.tm_mon, n.tm_mday, n.tm_hour, n.tm_min, n.tm_sec)

os.makedirs(f_dir + 'RISS' + '-' + s + '-' + '학위논문')

fc_name = f_dir + 'RISS' + '-' + s + '-' + '학위논문' + '\\' + 'RISS' + '-' + s + '-' + '학위논문' + '.csv'
fx_name = f_dir + 'RISS' + '-' + s + '-' + '학위논문' + '\\' + 'RISS' + '-' + s + '-' + '학위논문' + '.xls'

# 데이터 프레임 생성 후 xls , csv 형식으로 저장하기
import pandas as pd

df = pd.DataFrame()
df['번호'] = no2
df['제목'] = pd.Series(title2)
df['저자'] = pd.Series(author2)
df['소속(발행)기관'] = pd.Series(company2)
df['날짜'] = pd.Series(date2)
df['학위(논문일경우)'] = pd.Series(suksa2)
df['초록(논문일경우)'] = pd.Series(contents2)
df['자료URL주소'] = pd.Series(full_url2)

# xls 형태로 저장하기
df.to_excel(fx_name, index=False, engine='openpyxl')

# csv 형태로 저장하기
df.to_csv(fc_name, index=False)

print('요청하신 데이터 수집 작업이 정상적으로 완료되었습니다')