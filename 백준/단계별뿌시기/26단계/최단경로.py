import sys
import heapq
input = sys.stdin.readline
INF = sys.maxsize
V, e = map(int, input().split())
k = int(input())  # 시작점
dp = [INF] * (V + 1)  # 가중치 테이블 dp
heap = []
graph = [[] for _ in range(V + 1)]


def Dijstra(start):
    dp[start] = 0   # 가중치 테이블에서 시작 정점에 해당하는 가중치는 0으로 초기화
    heapq.heappush(heap, (0, start))
    while heap:
        wei, now = heapq.heappop(heap)
        if dp[now] < wei:   # 현재 테이블과 비교하여 불필요한 튜플이면 무시
            continue
        for w, next_node in graph[now]:
            # 현재 정점까지의 가중치 wei
            # 현재 정점에서 다음 정점까지의 가중치 w
            # Wei + w = 다음 노드까지의 가중치
            next_wei = w + wei
            if next_wei < dp[next_node]:    # 다음 노드까지의 가중치가 현재 기록된 값보다 작으면 조건 성립
                dp[next_node] = next_wei    # 계산했던 가중치를 업데이트 해준다.
                # 튜플로 묶어서 다음 가중치와 다음 점을 삽입해준다.
                heapq.heappush(heap, (next_wei, next_node))


for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # 가중치, 도착노드 형태로 저장한다.

Dijstra(k)
for i in range(1, V + 1):
    print("INF" if dp[i] == INF else dp[i])
