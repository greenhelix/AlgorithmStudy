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
https: // sungmin - joo.tistory.com / 33
https: // pacific-ocean.tistory.com/281
