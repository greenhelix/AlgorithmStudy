# https://www.acmicpc.net/problem/11650
n = int(input())
spot = []
for _ in range(n):
    a, b = map(int, input().split())
    spot.append([a, b])

for i in sorted(spot):
    print(*i)