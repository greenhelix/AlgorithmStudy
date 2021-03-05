# https://www.acmicpc.net/problem/3009
# 직사각형 구성중 네번째 점 구하기
from itertools import product
x, y = set(), set()
spot = []
for i in range(3):
    a, b = map(int, input().split())
    x.add(a)
    y.add(b)
    spot.append((a, b))
all = list(product(list(x), list(y)))
print(all)
answer = list(set(all) - set(spot))
print(answer[0][0], answer[0][1])
