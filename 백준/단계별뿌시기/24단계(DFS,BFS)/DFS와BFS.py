# https://www.acmicpc.net/problem/1260
# 깊이, 너비 탐색
N, M, V = map(int, input().split())
maps = [[0] * (N+1) for _ in range(N+1)]
print(maps)
for _ in range(M):
    link = list(map(int, input().split()))
    maps[link[0]][link[1]] = 1
    maps[link[1]][link[0]] = 1

print(maps)


def dfs(start, matrix, track):
    # start는 시작점을 의미한다. 1
    track += [start]
    # matrix[start] 시작점 1의 관계들을 의미
    for next in range(len(matrix[start])):
        if matrix[start][next] and next not in track:
            track = dfs(next, matrix, track)
    print(track)
    return track


def bfs(start):
    queue = [start]
    track = [start]

    while queue:
        now = queue.pop(0)
        for next in range(len(maps[now])):
            if maps[now][next] and next not in track:
                track += [next]
                queue += [next]
    print(track)
    return track


print(*dfs(V, maps, []))
print(*bfs(V))
