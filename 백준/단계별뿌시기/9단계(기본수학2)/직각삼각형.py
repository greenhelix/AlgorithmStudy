# https://www.acmicpc.net/problem/4153
# 피타고라스의 정의
while True:
    lines = list(map(int, input().split()))
    lines = sorted(lines)
    if sum(lines) == 0:
        break
    if (lines[0]**2 + lines[1]**2) == lines[2]**2:
        print('right')
    else:
        print('wrong')
