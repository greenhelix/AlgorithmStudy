# 주어진 도시들의 도로망에서 불필요한 도로를 제거하여 새로운 도시망을 구축한다.


roadRegister = [[False, True, True, False, False, False],
                [True, False, False, True, False, False],
                [True, False, False, False, False, False],
                [False, True, False, False, False, False],
                [False, False, False, False, False, True],
                [False, False, False, False, True, False]]


def solution(roads):

    connect = []

    # 각 도시들의 관계 도로를 정의한다. {작은 숫자도시, 큰 숫자 도시 } 관계로 한다.
    for i in range(len(roads)):
        for j in range(i + 1, len(roads)):  # i+1로 시작해야 이전 도시를 다시 검사 안한다.
            if roads[i][j]:
                connect.append({i, j})

    print(connect)

    # 연결되 도시들의 도로 수를 배경으로 새로운 관계망 지도를 만든다.
    new_roads = [[False for i in range(len(connect))]
                 for j in range(len(connect))]

    print(*new_roads, sep='\n')

    for i in range(len(new_roads)):
        for j in range(i + 1, len(new_roads)):
            if connect[i] & connect[j]:  # 해당 i, j번 도시들이 서로 연결 여부를 교집합 &으로 확인
                new_roads[i][j] = True
                new_roads[j][i] = True

    print(*new_roads, sep='\n')

    return new_roads


print(solution(roadRegister))
