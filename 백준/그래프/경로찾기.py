# 백준 11403번 (https://www.acmicpc.net/problem/11403)
# 그래프이론 / 플로이드-와샬
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
