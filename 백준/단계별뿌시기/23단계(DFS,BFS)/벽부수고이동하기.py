# https://www.acmicpc.net/problem/2206
# 6 4
# 0100
# 1110
# 1000
# 0000
# 0111
# 0000

from collections import deque
import sys
input = sys.stdin.readline
n, m = map(int, input().split())

matrix = [list(map(int, input())) for _ in range(n)]
# matrix = []
# for i in range(n):
#     matrix.append(list(map(int, list(input().strip()))))
print(*matrix, sep='\n')
# (1,1) -> (n, m)
# 최단경로 - 벽1, 이동가능0 - 벽 1개 부술때 최단경로가 더 짧다면 가능하다.
# 상하좌우로만 이동가능하다.
ud = [-1, 1, 0, 0]
rl = [0, 0, 1, -1]


def bfs():
    temp = deque()
    temp.append([0, 0, 1])

    short = [[[0]*2 for _ in range(m)] for _ in range(n)]
    short[0][0][1] = 1
    print(*short, sep='\n')

    while temp:
        x, y, wall = temp.popleft()

        if x == n - 1 and y == m - 1:
            print()
            print(*short, sep='\n')
            return short[x][y][wall]

        # 상하좌우 이동
        for i in range(4):
            xx = x + ud[i]
            yy = y + rl[i]

            if 0 <= xx < n and 0 <= yy < m:

                # 벽이다. 뚫을 기회가 있다.
                if matrix[xx][yy] == 1 and wall == 1:
                    short[xx][yy][0] = short[x][y][1] + 1
                    temp.append([xx, yy, 0])

                # 벽이 아니다.
                elif matrix[xx][yy] == 0 and short[xx][yy][wall] == 0:
                    short[xx][yy][wall] = short[x][y][wall] + 1
                    temp.append([xx, yy, wall])

    return - 1


print(bfs())
