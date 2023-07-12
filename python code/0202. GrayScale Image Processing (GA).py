import math
import os
from tkinter import *
from tkinter.filedialog import *
from tkinter.simpledialog import *

from tkinter import messagebox
## 함수 선언부
### 공통 함수부 ###
def loadImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    filename = askopenfilename(parent=window,
            filetypes=(("RAW파일", "*.raw"),("모든 파일", "*.*")))
    # 파일 크기 알아내기
    fSize = os.path.getsize(filename)  # Byte 단위
    inH = inW = int(math.sqrt(fSize))
    # 메모리 확보 (영상 크기)
    inImage = [[0 for _ in range(inW)] for _ in range(inH)]
    # 파일 --> 메모리 로딩
    rfp = open(filename, 'rb')
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




def zoomOutImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("축소배율", "" )
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH//scale;  outW = inW//scale;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    for i in range(inH) :
        for k in range(inW) :
            outImage[i//scale][k//scale] = inImage[i][k]
    ##############################
    displayImage()

def zoomInImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    scale = askinteger("확대배율", "")def moveImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    xVal = askinteger("X값", "")
    yVal = askinteger("Y값", "")
    for i in range(inH) :
        for k in range(inW) :
            if ( 0 <= i+xVal < outH ) and ( 0 <= k+yVal < outW) :
                outImage[i+xVal][k+yVal] = inImage[i][k]
    ##############################
    displayImage()
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH*scale;  outW = inW*scale;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    # for i in range(inH) :
    #     for k in range(inW) :
    #         outImage[i*scale][k*scale] = inImage[i][k]
    for i in range(outH) :
        for k in range(outW) :
            outImage[i][k] = inImage[i//scale][k//scale]
    ##############################
    displayImage()

def rotateImage() :
    global window, canvas, paper, filename
    global inImage, outImage, inH, inW, outH, outW
    angle = askinteger("각도", "0~360")
    # 중요! 출력이미지의 크기를 결정 --> 알고리즘에 따라서...
    outH = inH;  outW = inW;
    # 메모리 할당
    outImage = [[0 for _ in range(outW)] for _ in range(outH)]
    ## ** 찐 영상처리 알고리즘 ** ##
    radian = angle * math.pi / 180.0
    cx = inH//2
    cy = inW//2

    # for i in range(inH) :
    #     for k in range(inW) :
    #         newI = int(math.cos(radian)*(i-cx) - math.sin(radian)*(k-cy))+cx
    #         newK = int(math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy
    #
    #         if( 0<=newI<outH) and (0<=newK<outW) :
    #             outImage[newI][newK] = inImage[i][k]
    for i in range(outH) :
        for k in range(outW) :
            oldI = int(math.cos(radian)*(i-cx) + math.sin(radian)*(k-cy))+cx
            oldK = int(-math.sin(radian)*(i-cx) + math.cos(radian)*(k-cy))+cy

            if( 0<=oldI<inH) and (0<=oldK<inW) :
                outImage[i][k] = inImage[oldI][oldK]
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

image2Menu = Menu(mainMenu)
mainMenu.add_cascade(label='기하학 처리', menu=image2Menu)
image2Menu.add_command(label='이동', command=moveImage)
image2Menu.add_command(label='축소', command=zoomOutImage)
image2Menu.add_command(label='확대', command=zoomInImage)
image2Menu.add_command(label='회전', command=rotateImage)

window.mainloop()
