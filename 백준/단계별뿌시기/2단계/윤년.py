# https://www.acmicpc.net/problem/2753
# 수학/구현
# 윤년: 4의 배수, 100의 배수아닐때 or  4의 배수, 400 배수
year = int(input())
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(1)
        else:
            print(0)
    else:
        print(1)
else:
    print(0)
