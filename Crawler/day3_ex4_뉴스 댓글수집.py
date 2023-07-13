# Chap 16. 다양한 댓글 모으기
# 뉴스 기사의 댓글 모으기 - 미세먼지 / 스모그
# 테스트 기사 URL : https://news.naver.com/main/read.nhn?mode=LSD&mid=shm&sid1=102&oid=056&aid=0010661268

# Step 1. 필요한 모듈과 라이브러리를 로딩합니다.
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
import time
import math
import numpy
import pandas as pd
import random
import os
import re

# Step 2. 사용자에게 검색어 키워드를 입력 받고 저장할 폴더와 파일명을 설정합니다.
print("=" * 80)
print(" Chap 16.뉴스 기사의 댓글 정보  수집하기")
print("=" * 80)
print("\n")

query_txt = '뉴스기사댓글'
query_url = input('1.댓글을 크롤링할 뉴스의 URL을 입력하세요: ')
cnt = int(input('2.크롤링 할 건수는 몇건입니까?(10건단위로 입력): '))
page_cnt = math.ceil(cnt / 20)

f_dir = input("3.파일을 저장할 폴더명만 쓰세요(예:c:\\py_temp\\):")
if f_dir == '':
    f_dir = 'c:\\py_temp\\'

# 저장될 파일위치와 이름을 지정합니다
now = time.localtime()
s = '%04d-%02d-%02d-%02d-%02d-%02d' % (now.tm_year, now.tm_mon, now.tm_mday, now.tm_hour, now.tm_min, now.tm_sec)

os.makedirs(f_dir + s + '-' + query_txt)
os.chdir(f_dir + s + '-' + query_txt)

ff_name = f_dir + s + '-' + query_txt + '\\' + s + '-' + query_txt + '.txt'
fc_name = f_dir + s + '-' + query_txt + '\\' + s + '-' + query_txt + '.csv'
fx_name = f_dir + s + '-' + query_txt + '\\' + s + '-' + query_txt + '.xls'

# Step 3. 크롬 드라이버를 사용해서 웹 브라우저를 실행합니다.
s_time = time.time()

s = Service("c:/py_temp/chromedriver.exe")
driver = webdriver.Chrome(service=s)

driver.get(query_url)
driver.maximize_window()
time.sleep(5)

# Step 4. 현재 총 리뷰 건수를 확인하여 사용자의 요청건수와 비교 후 동기화합니다
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

result = soup.find('div', class_='u_cbox_head').find('span', 'u_cbox_count')
result2 = result.get_text()

print("=" * 80)
result3 = result2.replace(",", "")
result4 = re.search("\d+", result3)
search_cnt = int(result4.group())

if cnt > search_cnt:
    cnt = search_cnt

print("전체 검색 결과 건수 :", search_cnt, "건")
print("실제 최종 출력 건수", cnt)
print("실체 출력될 최종 페이지수", page_cnt)

# Step 5. 사용자가 요청한 건수가 많을 경우 리뷰 더보기 버튼을 클릭합니다
# 최초 10건 수집후 댓글 더보기 버튼 클릭
# 아래 버튼을 눌러 첫 화면에 총 20건의 댓글이 나오게 만듦
driver.find_element(By.XPATH, '//*[@id="cbox_module"]/div/div[9]/a/span[1]').click()
time.sleep(3)

# Step 6. 20건 출력되어 있는 현재 페이지 리뷰와 점수 등 내용 수집
writer_id2 = []  # 리뷰 작성자 ID
review2 = []  # 리뷰 내용
write_date2 = []  # 리뷰 작성 일자
gogam_0 = []  # 공감 횟수
gogam_1 = []  # 비공감 횟수
count = 0

for a in range(1, page_cnt + 1):

    if a == page_cnt:
        break
    else:
        driver.find_element(By.XPATH, '//*[@id="cbox_module"]/div/div[9]/a').click()
        time.sleep(3)
        print("%s페이지 이동 완료========================================================" % a)
        time.sleep(random.randrange(1, 3))  # 3-8 초 사이에 랜덤으로 시간 선택

print('이제 리뷰 정보를 수집합니다. 잠시만 기다려 주세요~~~~~~~~')

# txt 파일에 저장하기 위해 파일 open하기
f = open(ff_name, 'a', encoding='UTF-8')

html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')

reple_result = soup.find('div', class_='u_cbox_content_wrap').find('ul')
slist = reple_result.find_all('li')

for li in slist:
    count += 1
    print("\n")
    print("총 %s건 중 %s번째 댓글 수집 중입니다 ==================" % (cnt, count))

    writer_id = li.find('span', class_='u_cbox_nick').get_text()
    print("1.작성자ID:", writer_id)
    f.write("\n")
    f.write("총 %s 건 중 %s 번째 리뷰 데이터를 수집합니다==============" % (cnt, count) + "\n")
    f.write("1.작성자ID:" + writer_id + "\n")
    writer_id2.append(writer_id)

    try:
        review = li.find('span', class_='u_cbox_contents').get_text()
    except AttributeError:
        review = '작성자에 의해 삭제된 댓글입니다'
        print("2.리뷰 :", review)
    else:
        print("2.리뷰:", review)
    f.write("2.리뷰:" + review + "\n")
    review2.append(review)

    write_date = li.find('span', class_='u_cbox_date').get_text()
    print('3.작성일자:', write_date)
    f.write("3.작성일자:" + write_date + "\n")
    write_date2.append(write_date)

    gogam = li.find('div', class_='u_cbox_recomm_set').find_all('em')

    try:
        g_gogam = gogam[0].text
        print('4.공감:', g_gogam)
    except IndexError:
        g_gogam = '0'
        print('4.공감 :', g_gogam)
    f.write("4.공감:" + g_gogam + "\n")
    gogam_0.append(g_gogam)

    gogam = li.find('div', class_='u_cbox_recomm_set').find_all('em')

    try:
        b_gogam = gogam[1].text
        print('5.비공감:', b_gogam)
    except IndexError:
        b_gogam = '0'
        print('5.비공감 :', b_gogam)
    f.write("5.비공감:" + b_gogam + "\n")
    gogam_1.append(b_gogam)

    time.sleep(0.2)

    if count == cnt:
        break

# 학습목표 3. 수집된 데이터를 표 형태로 저장하기
# Step 7. xls 형태와 csv 형태로 저장하기
news_reple = pd.DataFrame()
news_reple['작성자ID'] = pd.Series(writer_id2)
news_reple['리뷰내용'] = pd.Series(review2)
news_reple['작성일자'] = pd.Series(write_date2)
news_reple['공감횟수'] = pd.Series(gogam_0)
news_reple['비공감횟수'] = pd.Series(gogam_1)

# csv 형태로 저장하기
news_reple.to_csv(fc_name, encoding="utf-8-sig", index=True)

# 엑셀 형태로 저장하기
news_reple.to_excel(fx_name, index=True, engine='openpyxl')

# Step 8. 요약 정보 출력하기
e_time = time.time()
t_time = e_time - s_time

print("\n")
print("=" * 120)
print("1.요청된 총 %s 건의 리뷰 중에서 실제 크롤링 된 리뷰수는 %s 건입니다" % (cnt, count))
print("2.총 소요시간은 %s 초 입니다 " % round(t_time, 1))
print("3.파일 저장 완료: txt 파일명 : %s " % ff_name)
print("4.파일 저장 완료: csv 파일명 : %s " % fc_name)
print("5.파일 저장 완료: xls 파일명 : %s " % fx_name)
print("=" * 120)

driver.close()