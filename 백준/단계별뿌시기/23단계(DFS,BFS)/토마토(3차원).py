# https://www.acmicpc.net/problem/7569
from collections import deque
m, n, h = map(int, input().split())
box = []
queue = deque()
ud, rl, fb = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]
for j in range(h):
    box.append([])
    for i in range(n):
        box[j].append(list(map(int, input().split())))
print(box)


def bfs():
    while queue:
        z, x, y = queue.popleft()
        for i in range(6):
            xx = x + ud[i]
            yy = y + rl[i]
            zz = z + fb[i]
            if 0 <= xx < n and 0 <= yy < m and 0 <= zz < h and box[zz][xx][yy] == 0:
                box[zz][xx][yy] = box[z][x][y] + 1
                queue.append([zz, xx, yy])


for 층 in range(h):
    for 세로 in range(n):
        for 가로 in range(m):
            if box[층][세로][가로] == 1:
                queue.append([층, 세로, 가로])

print(queue)


bfs()
print(box)
result = -2
isTrue = False
for z in box:
    for i in z:
        for j in i:
            if j == 0:
                isTrue = True
            result = max(result, j)

if isTrue == True:
    print('모두 익었다.')
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
