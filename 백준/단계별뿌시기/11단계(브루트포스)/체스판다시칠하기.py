# https://www.acmicpc.net/problem/1018
n, m = map(int, input().split())
board = []
for _ in range(n):
    board.append(input())
print(board)

# 세로가로 시작점을 고정해준다. 8이 넘어가면, 순차적으로 다음 세로칸부터 8칸을 측정
result = []
for i in range(n - 7):
    for j in range(m - 7):
        w, b = 0, 0
        # 시작점 i,j부 8칸을 설정해준다.
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0:
                    if board[k][l] != 'W':
                        w += 1
                    if board[k][l] != 'B':
                        b += 1
                else:
                    if board[k][l] != 'B':
                        w += 1
                    if board[k][l] != 'W':
                        b += 1
        result.append(w)
        result.append(b)
print(len(result))
print(result, '::', min(result))
