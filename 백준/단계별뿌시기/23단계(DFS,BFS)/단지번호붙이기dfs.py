# https://www.acmicpc.net/problem/2667
# 그래프이론 / 그래프탐색 / BFS / DFS
# 지도가 있고 1은 집이 있는 곳 , 0 은 없는 곳이다. 연결된 집의 모임인 단지를 정의 , 단지에 번호를 부여한다.
# 연결의 의미는 좌우 or 위아래 다른집이 있는 경우이다. 대각선은 연결 아님.
# 지도를 보고, 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬 출력.

from sys import stdin
n = int(input())
matrix = [[0] * n for _ in range(n)]
visited = [[0] * n for _ in range(n)]

for i in range(n):
    line = stdin.readline().strip()
    print(line)
    for j, b in enumerate(line):
        matrix[i][j] = int(b)

print(*matrix, sep='\n')
print(*visited, sep='\n')
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(a, b, c):
    visited[a][b] = 1  # 해당 a, b가 matrix에서 1이기 때문에 실행됐으므로 vistited도 1로 만들어준다.
    global nums  # 전역변수로 nums를 선언한다.
    print('global? = ', nums)
    if matrix[a][b] == 1:
        nums += 1
    for i in range(4):  # 방향벡트에 의해서 4가지 방향 범주로 반복문을 돌려준다.
        nx = a + dx[i]  # 해당 1의 좌표를 갖는 a, b에서 좌우, 위아래를 살펴준다.
        ny = b + dy[i]
        if 0 <= nx < n and 0 <= ny < n:  # 위의 방향으로 움직인 값이 n 범위 안에 있다면
            # 1인지 아닌지로 판단해준다. Visited는 그냥 비어있는지 확인
            if matrix[nx][ny] == 1 and visited[nx][ny] == 0:
                dfs(nx, ny, c)  # 다시 깊이탐색을 돌린다.


count = 1  # 해당 집의 수를 세줄 변수선언
numlist = []  # 단지의 수와 집의 갯수를 담는 리스트이다.
nums = 0  # 전역변수에 값을 부여 해준다.
# 7 * 7 사이즈의 지도이기 때문에 이중 For문을 활용한다.
for a in range(n):
    for b in range(n):
        if matrix[a][b] == 1 and visited[a][b] == 0:
            dfs(a, b, count)
            numlist.append(nums)
            nums = 0

print(len(numlist))
print('numlist = ', numlist)
for n in sorted(numlist):
    print(n)
