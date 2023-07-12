## 1. 입출력
import sys

# a,b = map(int,input().split())
# print(a+b)
# print(a-b)
# print(a*b)
# print(a//b)
# print(a%b)

# a = int(input())
# print(a-543)


# N = int(input())
# print(N, "* 1 =", N*1)
# print(N, "* 2 =", N*2)
# print(N, "* 3 =", N*3)
# print(N, "* 4 =", N*4)
# print(N, "* 5 =", N*5)
# print(N, "* 6 =", N*6)
# print(N, "* 7 =", N*7)
# print(N, "* 8 =", N*8)
# print(N, "* 9 =", N*9)

# e = int(input())
# if e >= 90 :
#     print("A")
# elif e>= 80 :
#     print("B")
# elif e>= 70 :
#     print("C")
# elif e>= 60 :
#     print("D")
# else:
#     print("F")


# H, M = map(int,input().split())
#
# if M < 45 :
#     if H == 0 :
#         H = 23
#         M += 60
#     else :
#         H -= 1
#         M += 60
# print(H, M-45)


# x = int(input())
# y = int(input())
#
# if x > 0 and y > 0 :
#     print(1)
# elif x > 0 and y < 0 :
#     print(4)
# elif x < 0 and y > 0 :
#     print(2)
# elif x < 0 and y < 0 :
#     print(3)


## 반복문
# n = int(input())
# for i in range(n,0,-1):
#     print("*"* i)

# n = int(input())
# a=0
# for i in range(1,n+1):
#     a+= i
# print(a)

# a = int(input())
# b = list(map(int,input().split()))
# print(min(b),max(b))

# a, b = map(int,input().split())
# if a > b :
#     print(">")
# elif a < b :
#     print("<")
# else :
#     print("==")

# y = int(input())
# if y % 4 == 0 and y % 100 != 0:
#     print(1)
# elif y % 400 == 0 :
#     print(1)
# else :
#     print(0)

# a, b, c = map(int,input().split())
# if a == b == c :
#     print(10000+a*1000)
# elif a == b or a == c :
#     print(1000+a*100)
# elif b == c :
#     print(1000+b*100)
# else :
#     print(max(a,b,c)*100)

# a = int(input())
# n = a//4
# print("long " *n + "int")

# n = int(input())
# for i in range(1,n):
#     print(" " * (n-i) + "*" * (2*i-1))
# for i in range(1,n+1):
#     print(" " * (i-1) + "*" *(2*(n-i)+1))


# n = int(input())
# for i in range(1,n+1):
#     print("*" * i + " " * (2*(n-i)) + "*" * i)
# for i in range(n,0,-1):
#     print("*" * (i-1) + " " * (2*(n-i+1)) + "*" * (i-1))

# n = int(input())
# for i in range(1,n+1):
#     print(" " * (i-1) + "*" * (2*(n-i)+1))
# for i in range(n-1,0,-1):
#     print(" " * (i-1) + "*" * (2*(n-i)+1))


# n = int(input())
# for i in range(1,n+1):
#     print(" " * (n-i) + "*" * i)
# for i in range(n-1,0,-1):
#     print(" " * (n-i) + "*" * i)

# h, m = map(int,input().split())
# t = int(input())
# h += t//60
# m += t%60
# if m >= 60:
#     m -= 60
#     h += 1
# if h > 23 :
#     h -= 24
#
# print(h, m)

# x,y= map(int,input().split())
# m=[31,28,31,30,31,30,31,31,30,31,30,31]
# w = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
# c=0
# for i in range(0,x-1):
#     c+=m[i]
# total_d=c+y
# print(w[total_d%7])


# for y in range(0, 5):
#     for x in range(0, y + 1):
#         print('*', end='')
#     print()
#
a = int(input())
for y in range(1,a+1) :
    for x in range(y):
        print("*",end="")
    print()

