# https://www.acmicpc.net/problem/1002
# https://leedakyeong.tistory.com/entry/%EB%B0%B1%EC%A4%80-1002%EB%B2%88-%ED%84%B0%EB%A0%9B-in-python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%BD%94%EB%93%9C-%EB%B0%8F-%EC%84%A4%EB%AA%85
from sys import stdin
t = int(input())
for _ in range(t):
    x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
    r = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    R = [r1, r2, r]
    mega = max(R)
    R.remove(mega)
    print(-1 if r == 0 and r1 == r2 else 0 if mega > sum(R)
          else 1 if r == (r1+r2) or mega == sum(R) else 2)


# from itertools import product
# from sys import stdin
# t = int(input())


# def find(r):
#     a = []
#     for i in range(r+1):
#         a.append(i)
#     for i in range(-1, -r - 1, -1):
#         a.append(i)
#     return a


# for _ in range(t):
#     x1, y1, r1, x2, y2, r2 = map(int, stdin.readline().split())
#     j, b = find(r1), find(r2)
#     jo = [x for x in product(j, j) if abs(x1 - x[0])+abs(y1-x[1]) == r1]  # 곱집합을 진행하면서 조건문을 달기위해선 이런식으로 사용한다.
# 곱집합은 원래 jo = list(prodcut(j,j)) 이런식으로 사용해도 무방하지만, 조건을 달고 싶다면 위와 같은 식으로 진행한다.
#     back = [y for y in product(b, b) if abs(x2 - y[0])+abs(y2-y[1]) == r2]
#     print(len(set.intersection(set(jo), set(back))))
