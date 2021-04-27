# https://programmers.co.kr/learn/courses/30/lessons/67260
from collections import deque


def solution(n, path, order):
    answer = True
    graph = {n: [] for n in range(n)}

    for s, e in path:
        graph[s].append(e)
        graph[e].append(s)

    print(graph, sep='\n')
    A, B = {}, {}

    for a, b in order:
        A[a] = b
        B[b] = a
        if b == 0:
            return False
        elif a == 0:
            A[0] = 0

    print('A:', A, '\nB:', B)

    # 방문기록 # 시작점 0 을 등록
    visited = [0] * n
    visited[0] = 1
    q = deque()
    q.append(0)

    while q:
        print('\nq:', q)
        print(visited)
        cur = q.popleft()
        if cur == A.get(B.get(cur)):
            visited[cur] = 2  # 방문횟수 증가
        else:
            print('now:', graph[cur])
            for i in graph[cur]:  # 각 노드의 도착지를 순회
                if visited[i] == 0:  # 해당 좌표가 방문기록이 없다.
                    q.append(i)  # 해당 좌표를 쌓아둔다(기록)
                    visited[i] = 1  # 방문횟수 등록

                    if A.get(i):
                        if visited[A[i]] == 2:
                            q.append(A[i])
                            visited[A[i]] = 1  # 방문횟수 감소

                        A[i] = 0  # 해당 경로는 초기화
            print('\nQ:', q)

    # 방문기록 검사
    for i in visited:
        if i == 0:  # 방문한 곳이 없는 방이 있는 경우 False
            return False
    return answer


n = 9
path = [[0, 1], [0, 3], [0, 7], [8, 1], [3, 6], [1, 2], [4, 7], [7, 5]]
order = [[8, 5], [6, 7], [4, 1]]

print(solution(n, path, order))

test = {8: 5, 6: 7, 4: 1}
print(test.get(4))
