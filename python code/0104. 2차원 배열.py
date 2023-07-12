import random
## 함수
def display() :
    for i in range(ROW):
        for k in range(COL):
            print("%3d " % image[i][k], end='')
        print()
    print()

## 변수
ROW, COL = 5, 5
image = None

## 메인
## 메모리 할당
image = [ ]
tmpAry = []
for i in range(ROW) :
    for k in range(COL) :
        tmpAry.append(0)
    image.append(tmpAry)
    tmpAry=[]

## 파일 --> 메모리로 로딩(Loading)
for i in range(ROW) :
    for k in range(COL) :
        pixel = random.randint(0,255)
        image[i][k] = pixel
display()

# 영상 처리
(1) 영상을 50 밝게 처리하자.
for i in range(ROW) :
    for k in range(COL) :
        if (image[i][k] + 50 > 255) :
            image[i][k] = 255
        else :
            image[i][k] += 50
display()

# 퀴즈 : 100 어둡게---------------------------
for i in range(ROW) :
    for k in range(COL) :
        if (image[i][k] - 100 < 0) :
            image[i][k] = 0
        else :
            image[i][k] = image[i][k] - 100
display()


# 퀴즈 : 완전 흑백 처리-------------------
for i in range(ROW) :
    for k in range(COL) :
        if (image[i][k] < 127) :
            image[i][k] = 255
        else :
            image[i][k] = 0
display()

# 퀴즈 : 완전 흑백 처리--------------------------------
hap = 0
for i in range(ROW) :
    for k in range(COL) :
        hap += image[i][k]
avg = hap / (ROW * COL)

for i in range(ROW) :
    for k in range(COL) :
        if (image[i][k] < avg) :
            image[i][k] = 255
        else :
            image[i][k] = 0
display()

# 퀴즈 : 반전하기-----------------------------------
for i in range(ROW) :
    for k in range(COL) :
        image[i][k] = 255 - image[i][k]

display()

## 과제1 : 흑백처리를 중앙값으로 하기 (퀵소트 구현, 선택 정렬)
