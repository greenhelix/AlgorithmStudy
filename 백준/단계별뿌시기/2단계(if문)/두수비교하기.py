# https://www.acmicpc.net/problem/1330
# 수학/구현
a, b = map(int, input().split())
if a > b:
    print('>')
elif a < b:
    print('<')
else:
    print('==')
