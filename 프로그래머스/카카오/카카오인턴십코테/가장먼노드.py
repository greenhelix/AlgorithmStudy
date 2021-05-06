# https://programmers.co.kr/learn/courses/30/lessons/49189
from collections import defaultdict, deque


def solution(n, edge):
    answer = 0
    dist = {node: 0 for node in range(1, n + 1)}
    print('dist:', dist)
    matrix = defaultdict(list)
    edge = sorted(edge)
    for no1, no2 in edge:
        matrix[no1].append(no2)
        matrix[no2].append(no1)
    print(matrix)
    matrix = dict(sorted(matrix.items()))
    print(matrix)

    # bfs
    q = deque(matrix[1])

    distance = 1
    print('==========bfs start==========')
    while q:
        print('q:', q)
        print('dist:', dist)
        for i in range(len(q)):
            print('change dist:', dist)
            node = q.popleft()
            print('\nnode:', node)

            # 출발점의 노드가 검출되면 그냥 측정을 안한다.
            if node == 1:
                continue

            # 해당 노드까지의 거리 축적확인 : 해당 노드의 축적된 거리가 0이라면 올린다.
            if dist[node] == 0:
                dist[node] = distance  # 초기값은 1을 반영
                # q에 축적된 해당 노드의 도착가능한 노드 정보 추가 입력
                for n in matrix[node]:
                    q.append(n)
                # 해당 노드의 작업이 끝났으므로 다음 node로 넘어간다.
                print('change q:', q)
        # 처음 들어온 q의 값들의 노드에 대한 거리 작업이 완료 됐으므로 다음
        # 노드로 넘어가서 작업을 계속 진행한다. 그리고 거리는 한칸 더 늘어난다.
        print(f'\n change distance {distance} -> {distance +1}')
        distance += 1
    print('==========bfs end==========')

    print('final dist:', dist)

    max_dist = max(dist.values())
    for i in dist.values():
        if i == max_dist:
            answer += 1

    return answer


n = 6
vertex = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]


def othersolution(n, edge):
    answer = 0
    graph = [[] for _ in range(n + 1)]
    dist = [0 for _ in range(n)]
    visit = [False for _ in range(n)]
    q, visit[0] = [0], True

    for a, b in edge:
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)

    print(graph)

    while q:
        i = q.pop()
        for j in graph[i]:
            if visit[j] == False:
                visit[j] = True
                q.append(j)
                dist[j] = dist[i] + 1

    dist.sort(reverse=True)
    print('dist:', dist)
    answer = dist.count(dist[0])
    return answer


print(solution(n, vertex))
print(othersolution(n, vertex))
