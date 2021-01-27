# https://www.acmicpc.net/problem/7569
from collections import deque
m, n, h = map(int, input().split())
box = []
queue = deque()
# 위아래,왼쪽오른쪽, 앞뒤 방향벡터
ud, rl, fb = [1, -1, 0, 0, 0, 0], [0, 0, 1, -1, 0, 0], [0, 0, 0, 0, 1, -1]

# 3차원 배열을 구성
for j in range(h):
    box.append([])
    for i in range(n):
        box[j].append(list(map(int, input().split())))

# 너비우선탐색


def bfs():
    while queue:
        z, x, y = queue.popleft()
        # 방향벡터에 맞게 진행한다. 층이 있다는 것을 유의하며 진행
        for i in range(6):
            xx = x + ud[i]
            yy = y + rl[i]
            zz = z + fb[i]
            if 0 <= xx < n and 0 <= yy < m and 0 <= zz < h and box[zz][xx][yy] == 0:
                box[zz][xx][yy] = box[z][x][y] + 1
                queue.append([zz, xx, yy])


# 3차원 배열에서 1을 찾아내어 큐에 해당 주소를 추가
for 층 in range(h):
    for 세로 in range(n):
        for 가로 in range(m):
            if box[층][세로][가로] == 1:
                queue.append([층, 세로, 가로])

# 1의 주소를 가진 queue를 bfs에서 감지하고 돌려 새로운 queue를 구성한다.
bfs()
result = -2
isTrue = False

# 3차원 배열을 검사하며 0의 유무와 걸린 일수의 최대값을 result에 담는다.
for z in box:
    for i in z:
        for j in i:
            if j == 0:
                isTrue = True
            result = max(result, j)

# 최종적으로 해당 3차원 배열에서 유추할 걸린 일 수를 보여준다.
if isTrue == True:
    print(-1)
elif result == -1:
    print(0)
else:
    print(result - 1)
