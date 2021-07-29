# https://www.acmicpc.net/problem/15552
# 수학/구현/사칙연산
import sys
case = int(input())

for i in range(0, case):
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)
