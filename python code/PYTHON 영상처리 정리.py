## 기본 사진에 영상처리 버튼 만들기
import math
import os
from tkinter import *
from tkinter import messagebox

## 함수
def displayImage() :
    global window, canvas, paper, height, width, filename  # global : 전역변
    if canvas != None :
        canvas.destroy()

    canvas = Canvas(window, height=512, width=512)
    paper = PhotoImage(height=512, width=512)
    canvas.create_image((512 / 2, 512 / 2), image=paper, state='normal')

    for i in range(height) :
        for k in range(width) :
            r = g = b = image[i][k]
            paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    canvas.pack()


# 버튼 함수 생성
def  lightImage() :  # 밝게
    for i in range(height):
        for k in range(width):
            if(image[i][k]+50>512):
                image[i][k] = 512
            else:
                image[i][k]+=50
    displayImage()

def  darkImage() :  # 어둡게
    for i in range(height):
        for k in range(width):
            if(image[i][k]-100<0):
                image[i][k] = 0
            else:
                image[i][k]-=100
    displayImage()

def  reverseImage() :  # 반전
    for i in range(height):
        for k in range(width):
            image[i][k] = 255 - image[i][k]
    displayImage()

def  black1Image() : # 흑백(127)
    for i in range(height):
        for k in range(width):
            if image[i][k] <127 :
                image[i][k] = 0
            else :
                image[i][k] = 512
    displayImage()

def  black2Image() :  # 흑백(평균값)
    hap=0
    for i in range(height):
        for k in range(width):
            hap+=image[i][k]
            avg=hap/(height*width)
            if image[i][k]<avg:
                image[i][k]=0
            else :
                image[i][k]= 512
    displayImage()


def black3Image(): # 흑백(중앙값)
    global image,height, width
    image1 = []
    for i in range(height):
        for k in range(width):
            a = image[i]
            b = a[k]
            image1.append(b)
    def quick_sort(image1):
        if len(image1) <= 1:
            return image1
        pivot = image1[len(image1) // 2]
        less, more, equal = [], [], []
        for each in image1:
            if each < pivot:
                less.append(each)
            elif each > pivot:
                more.append(each)
            else:
                equal.append(each)
        return quick_sort(less) + equal + quick_sort(more)

    # 중앙값 구하기
    rcm = (height * width) // 2
    med=(quick_sort(image1)[rcm]+quick_sort(image1)[rcm+1])/2
    # 최종
    for i in range(height):
        for k in range(width):
            if image[i][k] < med:
                image[i][k] = 0
            else:
                image[i][k] = 512
    displayImage()

#90도 회전
def rotate90():
    global image
    n=len(image)
    m=len(image[0])
    image1=[[0] * n for _ in range(m)]
    for i in range(n):
        for k in range(m):
            image1[k][n-i-1] = image[i][k]
    image = image1
    displayImage()

#180도 회전
def rotate180():
    global image
    n=len(image)
    m=len(image[0])
    image1=[[0] * n for _ in range(m)]
    for i in range(n):
        for k in range(m):
            image1[n-i-1][m-k-1] = image[i][k]
    image = image1
    displayImage()

#270도 회전
def rotate270():
    global image
    n=len(image)
    m=len(image[0])
    image1=[[0] * n for _ in range(m)]
    for i in range(n):
        for k in range(m):
            image1[m-k-1][i] = image[i][k]
    image = image1
    displayImage()

#상하 미러링
def udmirror():
    global image
    n=len(image)
    m=len(image[0])
    image1=[[0] * n for _ in range(m)]
    for i in range(n):
        for k in range(m):
            image1[n-i-1][k] = image[i][k]
    image = image1
    displayImage()

#좌우 미러링
def lrmirror():
    global image
    n=len(image)
    m=len(image[0])
    image1=[[0] * n for _ in range(m)]
    for i in range(n):
        for k in range(m):
            image1[i][m-k-1] = image[i][k]
    image = image1
    displayImage()


## 변수
window, canvas, paper = None, None, None
filename = ""
height, width = 0, 0
image = []

## 메인
window = Tk()
window.geometry('550x700')
window.title('영상처리 Alpha')

btnLight = Button(window, text ='밝게', command=lightImage )
btnLight.pack()

btnDark = Button(window, text ='어둡게', command=darkImage )
btnDark.pack()

btnRevese = Button(window, text ='반전', command=reverseImage )
btnRevese.pack()

btnBlack1 = Button(window, text ='흑백(127)', command=black1Image )
btnBlack1.pack()

btnBlack2 = Button(window, text ='흑백(평균값)', command=black2Image )
btnBlack2.pack()

btnBlack3 = Button(window, text ='흑백(중앙값)', command=black3Image )
btnBlack3.pack()

btnrotate90 = Button(window, text ='90도 회전', command=rotate90 )
btnrotate90.pack()

btnrotate180 = Button(window, text ='180도 회전', command=rotate180 )
btnrotate180.pack()

btnrotate270 = Button(window, text ='270도 회전', command=rotate270 )
btnrotate270.pack()

btnrotateup = Button(window, text ='상하 미러링', command=udmirror )
btnrotateup.pack()

btnrotatelr = Button(window, text ='좌우 미러링', command=lrmirror )
btnrotatelr.pack()


filename = 'Etc_Raw(squre)\흑백이미지.RAW'

# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))

# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]
# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))

rfp.close()
displayImage()
window.mainloop()