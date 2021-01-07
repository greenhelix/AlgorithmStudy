from collections import deque
# 백준 5431번
# https://www.acmicpc.net/problem/5431
a = int(input())
count = 0
for i in range(a):
    b = int(input())
    c = deque(list(map(int, input().split())))
    print(c)
    for j in range(b):
        if c[i] > c[j]:
            temp = c[j]
            del c[j]
            c.appendleft(temp)
            count += 1
            print(c)

print(count)
