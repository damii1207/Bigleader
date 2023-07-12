import math
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

from tkinter import messagebox
## 함수 선언부
### 공통 함수부 ###
def loadImage() :
    global window, canvas, paper, filename  # global = 전역변수를 사용하겠다
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window,
            filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*")))  # 원래 이렇게 씀 (안중요)

    # 파일 크기 알아내기
    fSize = os.path.getsize(filename)  # Byte 단위
    inH = inW = int(math.sqrt(fSize))
    # 메모리 확보 (영상 크기)
    inImage = [[0 for _ in range(inW)] for _ in range(inH)]
    # 파일 --> 메모리 로딩
    rfp = open(filename, 'rb')  # rb = read birary = 바이너리 파일 읽기
    for i in range(inH):
        for k in range(inW):
            inImage[i][k] = ord(rfp.read(1))

    rfp.close()
    equalImage()

def displayImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    if canvas != None :
        canvas.destroy()
    window.geometry(str(outH) + 'x' + str(outW))
    canvas = Canvas(window, height=outH, width=outW)
    paper = PhotoImage(height=outH, width=outW)
    canvas.create_image((outH / 2, outW / 2), image=paper, state='normal')
    # for i in range(outH) :
    #     for k in range(outW) :
    #         r = g = b = outImage[i][k]
    #         paper.put('#%02x%02x%02x' % (r, g, b), (k, i))
    rgbString = ""
    for i in range(outH) :
        tmpString = ""
        for k in range(outW) :
            r = g = b = outImage[i][k]
            tmpString += '#%02x%02x%02x ' % (r, g, b)
        rgbString += '{' + tmpString + '} '
    paper.put(rgbString)

    canvas.pack()

def saveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    saveFp = asksaveasfile(parent=window, mode='wb',
        defaultextension='*.raw',
        filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*")))
    import struct
    for i in range(outH) :
        for k in range(outW) :
            saveFp.write( struct.pack('B', outImage[i][k]))
    saveFp.close()
    messagebox.showinfo('성공',  saveFp.name + '으로 저장')

## 영상 처리 함수부 ##
def equalImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = inImage[i][k]
    ##############################
    displayImage()

def reverseImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            outImage[i][k] = 255- inImage[i][k]
    ##############################
    displayImage()

def addImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력 이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    value = askinteger("밝게할 값", "-255 부터 255까지 입력", minvalue=-255, maxvalue=255)
    for i in range(inH) :
        for k in range(inW) :
            if (inImage[i][k] + value > 255) :
                outImage[i][k] = 255
            elif (inImage[i][k] + value < 0) :
                outImage[i][k] = 0
            else :
                outImage[i][k] = inImage[i][k] + value
    ##############################
    displayImage()

## 전역 변수부
window, canvas, paper = None, None, None
filename = ""
inImage, outImage = None, None
inH, inW, outH, outW = 0, 0, 0, 0

## 메인 코드부
window = Tk()
window.geometry('300x300')
window.title('GrayScale Image Processing (Beta 1)')

mainMenu = Menu(window) # 메뉴의 틀
window.config(menu=mainMenu)

fileMenu = Menu(mainMenu) # 상위 메뉴(파일)
mainMenu.add_cascade(label='파일', menu=fileMenu)
fileMenu.add_command(label='열기', command=loadImage)
fileMenu.add_command(label='저장', command=saveImage)
fileMenu.add_separator()
fileMenu.add_command(label='종료', command=None)

image1Menu = Menu(mainMenu)
mainMenu.add_cascade(label='영상처리1', menu=image1Menu)
image1Menu.add_command(label='동일영상', command=equalImage)
image1Menu.add_command(label='반전', command=reverseImage)
image1Menu.add_command(label='밝게/어둡게', command=addImage)


# ##흑백
# blackMenu = Menu(mainMenu)
# mainMenu.add_cascade(label='흑백', menu=blackMenu)
# blackMenu.add_command(label='127', command=black1Image)
# blackMenu.add_command(label='평균값', command=black2Image)
# blackMenu.add_command(label='중앙값', command=black3Image)


window.mainloop()

## 퀴즈 : 흑백 3종류

# # 영상처리 알고리즘 분류
#  - 화소점 처리(Pixel Processing)
#  : 동일 영상, 반전, 흑백, 감마, 파라볼라,,,,
#  - 기하학 처리(Geometry Processing)
#  : 이동, 회전, 축소, 확대
#  - 화소영역 처리(Area Processing)
#  : 블러링, 샤프닝, 경계선 처리, 지문 인식,,,
#  - 히스토그램 처리 (Histogram Processing) --> 화소점 처리의 일부
#  : 흑백(평균값, 중앙값), 평활화



