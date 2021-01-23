# https://www.acmicpc.net/problem/7576
# 그래프 이론/ 그래프 탐색  너비 우선 탐색
from collections import deque
m, n = map(int, input().split())
box = []
queue = deque()
updown, rightleft = [1, -1, 0, 0], [0, 0, -1, 1]
# 1 익은 토마토 0 안익은 토마토 -1 비어있는 칸
# 모두 익지 못하는 상황 -1 / 이미 모두 익어있는 상황 1
for i in range(n):
    box.append(list(map(int, input().split())))
print(*box, sep='\n')


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            xx = x + updown[i]
            yy = y + rightleft[i]
            if 0 <= xx < n and 0 <= yy < m and box[xx][yy] == 0:
                box[xx][yy] = box[x][y] + 1
                queue.append([xx, yy])


for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            queue.append([i, j])

bfs()
print(*box, sep='\n')
isTrue = False
result = -2
for i in box:
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
