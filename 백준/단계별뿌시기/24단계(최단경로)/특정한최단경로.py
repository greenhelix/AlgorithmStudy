import heapq
import sys
input = sys.stdin.readline
N, E = map(int, input().split())
matrix = {i: dict() for i in range(1, N+1)}
for _ in range(E):
    a, b, c = map(int, input().split())
    matrix[a].update({b: c})
    matrix[b].update({a: c})
v1, v2 = map(int, input().split())

print(f'노드갯수: {N}, 경로갯수: {E}\n정점1: {v1}, 정점2: {v2}')
print('Map', *matrix.items(), sep='\n')
print('===================================')


def dijkstra(start: int):

    short = {node: float('inf') for node in matrix.keys()}
    short[start] = 0
    temp = []
    heapq.heappush(temp, [short[start], start])  # 거리, 노드를 넣어준다.

    while temp:
        sd, s = heapq.heappop(temp)

        for e, ed in matrix[s].items():
            dist = sd + ed

            if dist < short[e]:
                short[e] = dist
                heapq.heappush(temp, [dist, e])
    print(short)
    return short


one = dijkstra(1)
V1 = dijkstra(v1)
V2 = dijkstra(v2)
result = min(one[v1] + V1[v2] + V2[N], one[v2] + V2[v1] + V1[N])
print(result if result < sys.maxsize else -1)
