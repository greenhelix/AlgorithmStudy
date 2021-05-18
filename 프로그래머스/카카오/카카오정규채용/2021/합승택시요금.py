import heapq
# from collections import deque
n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [
    5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

n2, s2, a2, b2 = 7,	3,	4,	1
fares2 = [[5, 7, 9], [4, 6, 4], [3, 6, 1], [3, 2, 3], [2, 1, 6]]

n3, s3, a3, b3 = 6, 4, 5, 6,
fares3 = [[2, 6, 6], [6, 3, 7], [4, 6, 7], [6, 5, 11],
          [2, 5, 12], [5, 3, 20], [2, 4, 8], [4, 3, 9]]

matrix = dict()


def dijkstra(start, end):

    n = len(matrix)
    # 빈공간
    temp = [float('inf') for i in range(n)]

    temp[start] = 0
    heap = [[0, start]]

    while heap:

        cost, node = heapq.heappop(heap)
        if temp[node] < cost:
            continue
        for item in matrix[node]:
            nextNode, nextCost = item[0], item[1]
            nextCost += cost
            if nextCost < temp[nextNode]:
                temp[nextNode] = nextCost
                heapq.heappush(heap, [nextCost, nextNode])

    return temp[end]


def solution(n, s, a, b, fares):
    # 0원으로 하면 안된다, 값이 없는경우는 무시하기 위해 inf로 기본 값을 해준다.
    total = float('inf')
    global matrix  # 전역변수로 지정
    # 리스트를 통해 맵을 만든다. 범위는 노드번호를 고려하여 1부터 진행한다.
    matrix = [[] for i in range(n+1)]

    for i, j, k in fares:
        matrix[i].append([j, k])
        matrix[j].append([i, k])

    print(*matrix, sep='\n')

    for i in range(1, n + 1):
        check = dijkstra(s, i) + dijkstra(i, a) + dijkstra(i, b)
        total = min(total, check)
        print(f'합승구간이 {s}->{i}일 때, 다익스트라 {check}원, \n총 요금은 {total}원 입니다.')

    return total


print(f'최소값은 {solution(n, s, a, b, fares)}원 입니다.')

print(f'최소값은 {solution(n2, s2, a2, b2, fares2)}원 입니다.')

print(f'최소값은 {solution(n3, s3, a3, b3, fares3)}원 입니다.')
