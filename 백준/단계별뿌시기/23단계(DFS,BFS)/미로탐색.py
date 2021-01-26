# https://www.acmicpc.net/problem/2178
# BFS, DFS, 그래프 이론, 그래프 탐색
# 4 6
# 101111
# 101010
# 101011
# 111011
n, m = map(int, input().split())
matrix = []
queue = []
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
for i in range(n):
    matrix.append(list(input()))
queue = [[0, 0]]
matrix[0][0] = 1
print('map')
print(*matrix, sep='\n')
print('========')
while queue:
    a, b = queue[0][0], queue[0][1]
    del queue[0]
    for i in range(4):
        x = a + dx[i]
        y = b + dy[i]
        if 0 <= x < n and 0 <= y < m and matrix[x][y] == "1":
            queue.append([x, y])
            matrix[x][y] = matrix[a][b] + 1
            print(x, y)
            print('matrix[x][y]=', matrix[x][y])
print(*matrix, sep='\n')
print(matrix[n - 1][m - 1])
# from sys import stdin
# n, m = map(int, input().split())
# print(n, m)
# matrix = [[0] * m for _ in range(n)]
# print(*matrix, sep='\n')
# for i in range(n):
#     line = stdin.readline().strip()
#     for j, k in enumerate(line):
#         matrix[i][j] = int(k)
# print('map')
# print(*matrix, sep='\n')
# print('========')

# updownx = [1, -1, 0, 0]
# rightlefty = [0, 0, -1, 1]

# queue = []
# queue = [[0, 0]]
# matrix[0][0] = 1
# while queue:
#     a, b = queue[0][0], queue[0][1]
#     del queue[0]
#     for i in range(4):  # 방향 탐색
#         x = a + updownx[i]
#         y = b + rightlefty[i]
#         if 0 <= x < n and 0 <= y < m and matrix[x][y] == 1:
#             queue.append([x, y])
#             matrix[x][y] = matrix[a][b] + 1
#             print(x, y)
#             print('matrix[x][y]=', matrix[x][y])

# print(*matrix, sep='\n')
# print(matrix[n - 1][m - 1])
