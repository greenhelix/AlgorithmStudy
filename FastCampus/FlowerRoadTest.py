N = 6
G = [[1, 0, 2, 3, 3, 4],
     [1, 1, 1, 1, 1, 1], [0, 0, 1, 1, 1, 1], [3, 9, 9, 0, 1, 99], [9, 11, 3, 1, 0, 3], [12, 3, 0, 0, 0, 1]]
ans = 10000
dx, dy = [0, 0, 0, 1, -1], [0, 1, -1, 0, 0]


def ck(lst):
    ret = 0
    flow = []
    for flower in lst:
        x = flower // N
        y = flower % N

        if x == 0 or x == N - 1 or y == 0 or y == N - 1:
            return 10000

        for w in range(5):
            flow.append((x + dx[w], y + dy[w]))
            ret += G[x + dx[w]][y + dy[w]]
    if len(set(flow)) != 15:
        return 10000
    return ret


for i in range(N * N):
    for j in range(i+1, N * N):
        for k in range(j+1, N * N):
            ans = min(ans, ck([i, j, k]))

print(ans)
