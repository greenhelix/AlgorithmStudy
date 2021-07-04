import time
# from collections import defaultdict
# start1 = time.time()
# global n, m, graph

# n, m, v = map(int, input().split())

# graph = defaultdict(set)

# for i in range(m):
#     x, y = map(int, input().split())
#     graph[x].add(y)
#     graph[y].add(x)


# def dfs(v):
#     print(v, end=" ")
#     for i in graph[v]:
#         if i not in track:
#             track.append(i)
#             dfs(i)


# def bfs(v):
#     stack = []
#     result = []
#     stack.append(v)
#     result.append(v)
#     while stack:
#         sp = stack.pop(0)
#         print(sp, end=" ")
#         for i in graph[sp]:
#             if i not in result:
#                 stack.append(i)
#                 result.append(i)


# track = []
# track.append(v)

# dfs(v)
# print()
# bfs(v)
# print(time.time() - start1)

start2 = time.time()
N, M, V = map(int, input().split())
maps = [[0] * (N+1) for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    maps[x][y] = 1
    maps[y][x] = 1

print(maps)


def dfs(start, matrix, track):
    track += [start]
    for next in range(len(matrix[start])):
        if matrix[start][next] and next not in track:
            track = dfs(next, matrix, track)
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
    return track


print(*dfs(V, maps, []))
print(*bfs(V))
print(time.time()-start2)
