from bs4 import BeautifulSoup
ex1 = '''
<html>
    <head>
        <title> HTML 연습 </title>
    </head>
    <body>
        <p align="center"> text 1 </p>
        <p align="right"> text 2 </p>
        <p align="left"> text 3 </p>
        <img src="c:\\temp\\image\\솔개.png">
    </body>
<html> '''

soup = BeautifulSoup(ex1, 'html.parser')
# soup.find('태그명',속성명 = '속성값')
soup.find('p',align = 'right').get_text().strip()
soup.find_all('p')[1].get_text().strip()

# for i in soup.find_all('p') :
#     print(i.get_text().strip().replace('text','txt'))

x = soup.find_all('p')
for idx, i in enumerate(x, start=1) :
    print(idx, i.get_text().strip())


# # 웹 제어를 위한 크롬드라이버 설정 1
# # 크롬드라이버 자동 다운로드
# # pip install chromedriver-autoinstaller
# from selenium import webdriver
# import chromedriver_autoinstaller as ca
# driver = webdriver.Chrome(ca.install())
#
# # 웹 제어를 위한 크롬드라이버 설정 2
# # 크롬드라이버 수동 다운로드 및 활용
# from selenium import webdriver
# driver = webdriver.Chrome('c:/py_temp/chromedriver.exe')
#
# # 웹 제어를 위한 크롬드라이버 설정3
# # 파이썬 3.10 이상 버전
# from selenium import webdriver
# driver = webdriver.Chrome()


