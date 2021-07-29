# https://www.acmicpc.net/problem/8393
# 수학/구현
n = int(input())
if n % 2 != 0:
    print((n // 2) * (n + 1) + (n // 2 + 1))
else:
    print((n//2)*(n+1))
