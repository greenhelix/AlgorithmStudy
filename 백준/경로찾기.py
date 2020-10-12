# 가중치없는방향그래프G가주어졌을때, 모든정점(i, j)에대해서, i에서j로가는경로가있는지없는지구하는프로그램을작성하시오.

# 첫째줄에정점의개수N(1 ≤ N ≤ 100)이주어진다.둘째줄부터N개줄에는그래프의인접행렬이주어진다.
# i번째줄의j번째숫자가1인경우에는i에서j로가는간선이존재한다는뜻이고, 0인경우는없다는뜻이다.i번째줄의i번째숫자는항상0이다.

# 총N개의줄에걸쳐서문제의정답을인접행렬형식으로출력한다.정점i에서j로가는경로가있으면i번째줄의j번째숫자를1로, 없으면0으로출력해야한다.

# 3
# 0 1 0
# 0 0 1
# 1 0 0

# 1 1 1
# 1 1 1
# 1 1 1
N = int(input())
path = [[0 for column in range(0, N)] for row in range(0, N)]

for i in range(0, N):
    for j, m in enumerate(map(int, input().split())):
        path[i][j] = m

print(path)

for k in range(0, N):
    for i in range(0, N):
        for j in range(0, N):
            if path[i][k] and path[k][j]:
                path[i][j] = 1

for i in range(0, N):
    _str = ""
    for j in range(0, N):
        _str += str(path[i][j]) + " "
    print(_str)
