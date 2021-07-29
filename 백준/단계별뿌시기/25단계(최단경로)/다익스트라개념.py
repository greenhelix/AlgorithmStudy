import heapq


def dijkstra(country, startPoint, endPoint):

    # 최적화된 도로망이라는 country_opt_road 배열을 선언과 동시에 inf로 비어있는 상태로
    # 선언해준다. input 되는 country에 있는 노드를 찾아서 포인트별로 저장하고
    # 그 안의 값들은 일단 inf로 초기화 하는 작업의 코드
    country_opt_road = {node: float('inf') for node in country}

    # 최초 출발점은 input되는 startPoint로 설정하여 0으로 설정한다.
    country_opt_road[startPoint] = 0

    # 잠시 데이터를 쌓아둘 공간을 설정한다.
    heap = []

    # 이 heap공간에 Startpoint지점의 정보와 거리 0을 넣어준다.
    heapq.heappush(heap, [country_opt_road[startPoint], startPoint])

    # heap이 텅텅 빌때까지 반복한다.
    while heap:

        # 최초 출발점을 꺼낸뒤 이후 들어오는 노드와 거리를 꺼내온다.
        거리1, 출발지 = heapq.heappop(heap)

        print('출발지:', 출발지, '거리', 거리1)
        if country_opt_road[출발지] < 거리1:
            continue

        # 1. mycountry의 매트리스에서 해당 노드에서 이동할 수 있는 노드와 거리를 가져온다.
        # ex) 'A' :{'B':8} --> 'A'노드에서 'B'로 이동이 되고 거리는  8 이다.

        for 도착지, 거리2 in country[출발지].items():

            # 최적 거리인지 확인하기 위해 선택한 노드까지의 거리를 먼저 저장한다.
            distance = 거리1 + 거리2
            print('------------------------------')
            print('도착지:', 도착지, '거리', 거리2)

            # 최적화를 하기 위해 조건문으로 더 짧은 길을 찾는 가정문
            if distance < country_opt_road[도착지]:

                print('최적화 작업 발생', 도착지, '포인트에서 발생')

                country_opt_road[도착지] = distance
                heapq.heappush(heap, [distance, 도착지])
                print(도착지, ':::', country_opt_road)
                print('heap:', heap)
                print('======================')

        print('**********************reset')

    print()
    print('final ----------------------')


mycountry = {'A': {'B': 8, 'C': 1, 'D': 2}, 'B': {}, 'C': {
    'B': 5, 'D': 2}, 'D': {'E': 3, 'F': 5}, 'E': {'F': 1}, 'F': {'A': 5}}

print(dijkstra(mycountry, 'A', 'F'))


def dijkstra_road(matrix, start, end):
    search_load = {node: [float('inf'), start] for node in matrix}
    search_load[start] = [0, start]
    print('초기값:', search_load)

    # 최적화 길의 노드들을 저장하기 위한 리스트 선언합니다.
    temp = []
    heapq.heappush(temp, [search_load[start][0], start])
    print('초기큐:', temp)

    while temp:

        현재거리, 현재노드 = heapq.heappop(temp)
        print('노드:', 현재노드, '거리:', 현재거리)

        if search_load[현재노드][0] < 현재거리:
            continue

        for 노드, 거리 in matrix[현재노드].items():

            최신거리 = 현재거리 + 거리
            print('최신거리:', 최신거리)

            if 최신거리 < search_load[노드][0]:
                print('더 짧은 거리 발견')
                search_load[노드] = [최신거리, 현재노드]
                heapq.heappush(temp, [최신거리, 노드])

    # 출발점으로부터 해당 노드까지의 거리를 나타내고,
    # 경로를 알기 위해서는 아래와 같이 역 추적으로 노드를 구해내면 됩니다.
    print('최종값:', search_load)
    opt_path = []
    opt_path.append(end)
    path = end
    while search_load[path][1] != start:
        opt_path.append(search_load[path][1])
        path = search_load[path][1]

    opt_path.append(start)

    print(opt_path)
    return '->'.join(opt_path[::-1])


print(dijkstra_road(mycountry, 'A', 'F'))
