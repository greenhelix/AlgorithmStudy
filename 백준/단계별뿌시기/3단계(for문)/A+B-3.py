# https://www.acmicpc.net/problem/10950
# 수학/구현/사칙연산
case = int(input())

for i in range(0, case):
    a, b = map(int, input().split())
    print(a + b)
