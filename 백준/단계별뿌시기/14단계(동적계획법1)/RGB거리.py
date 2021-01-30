# https://www.acmicpc.net/problem/1149
# 집이 n개 있다. 거리는 선분으로, 1~n번 집순서대로 있음.
# 빨 , 초, 파 중 하나의 색으로 칠해야함.
# 각 색별로 비용이 주어짐.
# 규칙 : 1번집의 색은 2번 집의 색과 달라야한다.
# 규칙 : n번집의 색은 n-1번 집의 색과 달라야 한다.
# 규칙 : i번 집의 색은 i-1번, i+1번 집의 색과 달라야 한다.

n = int(input())
p = []
for i in range(n):
    p.append(list(map(int, input().split())))

for i in range(1, len(p)):
    p[i][0] = min(p[i - 1][1], p[i - 1][2]) + p[i][0]
    print(p[i][0], i)
    p[i][1] = min(p[i - 1][0], p[i - 1][2]) + p[i][1]
    p[i][2] = min(p[i - 1][0], p[i - 1][1]) + p[i][2]

print(min(p[n - 1][0], p[n - 1][1], p[n - 1][2]))
