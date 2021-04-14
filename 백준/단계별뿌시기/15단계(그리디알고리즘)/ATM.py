# https://www.acmicpc.net/problem/11399

n = int(input())
time = list(map(int, input().split()))
print(time)
time = sorted(time)
print(time)
re, moment = 0, 0
for i in time:
    moment += i
    re += moment

print(re)
