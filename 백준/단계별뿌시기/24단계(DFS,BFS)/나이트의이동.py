from collections import deque


def bfs(sx, sy, fx, fy):
    # 방향의종류는 총 8가지이다. 이것을 고려해서 X의 값을 2번 반복하여 나열하고
    # y의 값을 맞춰 나열한다. --> 더 간단한 방법있으면 꼭 찾아 두자.
    vectorx = [-2, 2, -1, 1, -2, 2, -1, 1]
    vectory = [-1, 1, -2, 2, 1, -1, 2, -2]
    queue = deque()
    queue.append([sx, sy])
    board[sx][sy] = 1

    while queue:
        x, y = queue.popleft()

        # 반복을 빠져나오게 해주는게 좋다.
        if x == fx and y == fy:
            return board[x][y] - 1

        for i in range(8):
            xx = x + vectorx[i]
            yy = y + vectory[i]

            if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 0:
                board[xx][yy] = board[x][y] + 1
                queue.append((xx, yy))


test = int(input())
while test:

    n = int(input())
    board = [[0] * n for _ in range(n)]
    sx, sy = map(int, input().split())
    fx, fy = map(int, input().split())

    # 불필요한 테스트케이스는 빠르게 넘어갈 수 있게 해준다.
    if sx == fx and sy == fy:
        print(0)
        test -= 1
        continue

    print(bfs(sx, sy, fx, fy))
    test -= 1
