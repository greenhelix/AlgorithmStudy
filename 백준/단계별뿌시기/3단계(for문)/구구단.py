# https://www.acmicpc.net/problem/2739]
# 수학/구현/사칙연산
N = int(input())
s = 1
while s < 10:
    print(N, '*', s, '=', int(N * s))
    s += 1
