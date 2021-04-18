# https://www.acmicpc.net/problem/13305
n = int(input())
road = list(map(int, input().split()))
city = list(map(int, input().split()))

won, h = 0, city[0]

for i in range(len(road)):
    if city[i] <= h:
        h = city[i]
    won += h * road[i]

print(won)
