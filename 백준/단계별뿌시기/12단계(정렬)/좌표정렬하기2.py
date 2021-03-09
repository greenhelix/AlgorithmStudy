# https://www.acmicpc.net/problem/11651
n = int(input())
spot = []
for _ in range(n):
    a, b = map(int, input().split())
    spot.append([b, a])
for i in sorted(spot):
    print(i[1], i[0])
