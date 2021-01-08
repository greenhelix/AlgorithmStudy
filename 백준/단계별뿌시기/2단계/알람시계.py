# https://www.acmicpc.net/problem/2884
# 수학/사칙연산
H, M = map(int, input().split())
temp = M - 45
if temp < 0:
    M = 60 + temp
    H -= 1
    if H < 0:
        H = 23
        print(H, M)
    else:
        print(H,  M)
else:
    M = temp
    print(H, M)
