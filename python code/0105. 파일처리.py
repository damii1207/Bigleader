## 파일을 2가지
# 텍스트 파일 - 아스키 코드
# 바이너리 파일 -> 이미지 파일 중 raw 파일(1byte = 1픽셀 1바이트 숫자로 표현할수 있느 범위 -128 127
# - 이진파일 / 텍스트파일을 제외한 파일 / 고유의 소프트웨어가 필요
## row * row = byte
import os.path
import math

filename = 'Etc_Raw(squre)\LENA256.RAW'

# 파일 크기 알아내기
fSize = os.path.getsize(filename) # Byte 단위
height = width = int(math.sqrt(fSize))
print(height, 'x', width)

# 메모리 확보 (영상 크기)
image = [ [0 for _ in range(width)] for _ in range(height)]

# 파일 --> 메모리 로딩
rfp = open(filename, 'rb')
for i in range(height) :
    for k in range(width) :
        image[i][k] = ord(rfp.read(1))  # 1바이트씩 읽어서 문자를 0~225사이로 하는게 ord
rfp.close()

## 일부만 확인
for i in range(100, 105, 1):
    for k in range(100, 105, 1):
        print("%3d " % image[i][k], end='')
    print()
print()

## 반전 처리
for i in range(height) :
    for k in range(width) :
        image[i][k] = 255 - image[i][k]

for i in range(100, 105, 1):
    for k in range(100, 105, 1):
        print("%3d " % image[i][k], end='')
    print()
print()

# # 퀴즈 : 흑백처리
# for i in range(height) :
#     for k in range(width) :
#         if image[i][k] <127.5):
#           image[i][k] = 0
#         else :
#             image[i][k] = 255

