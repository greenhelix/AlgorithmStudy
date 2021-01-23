# https://www.acmicpc.net/problem/1753
# 그래프 이론 / 다익스트라
# 방향그래프 - 시작점에서 모든 정점의 차단 경로 구하기 - 가주치는 10이하의 자연수
# 정점의 갯수 v 간선의 갯수 e ,시작점 k
# e개줄의 각 간선을 나타내느 세 개의 정수 ( u, v, w )
# u - v 로 가는 가중치 w 라는 의미 ( u != v, w<=10 )
# 서로다른 두 정점 사이에 여러 개의 간서이 존재할 수 있다.

v, e = map(int, input().split())
k = int(input())
matrix = {}
for i in range(v):
    matrix[i + 1] = set()
for j in range(e):
    u, v, w = map(int, input().split())
    matrix[u].add((v, w))
    matrix[v].add((u, w))

for s, e in matrix.items():
    print("{} : {}".format(s, e))

# 첫째줄부터 v개 줄에 걸쳐, i번째줄에 i번 정점으로의 최단 경로값을 출력
# # 시작점은 0 , 경로없는경우 INF출력
# from heapq import heappush, heappop
# inf = 100000000
# sample =[
# [5, 1, 1],
# [1, 2, 2],
# [1, 3, 3],
# [2, 3, 4],
# [2, 4, 5],
# [3, 4, 6]]
# v, e = 5, 6
# k = 1
# s = [[] for _ in range(v + 1)]
# dp = [inf] * (v + 1)
# heap = []
# def dijkstra(start):
#     dp[start] = 0
#     heappush(heap, [0, start])
#     while heap:
#         w, n = heappop(heap)
#         for n_n, wei in s[n]:
#             n_w = wei + w
#             if n_w < dp[n_n]:
#                 dp[n_n] = n_w
#                 heappush(heap, [n_w, n_n])
# for i in range(e):
#     u, v, w = map(int, sample[i])
#     s[u].append([v, w])
# dijkstra(k)
# for i in dp[1:]:
#     print(i if i != inf else "INF")
