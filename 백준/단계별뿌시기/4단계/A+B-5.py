# https://www.acmicpc.net/problem/10952
# 구현 / 수학 / 사칙연산
while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)
