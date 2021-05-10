# 주어진 그래프의 길들이 나열되어 있다. 이 길들은 양방향을 의미한다.
# 정복은 맨 외곽의 도시부터 진행된다. day  = 1이다.
# 이런식으로 안으로 들어가며 도시가 점령된는 시간을 각 도시별로 배열로 표현한다.
# 그러나 도시들의 길이 서로 순환하는 관계라면 점령이 불가능하다. 그래서 -1로 표현된다.

# 그래프 순환에 대한 풀이 --> 순환을 굳이 구현하지말고 규칙을 반영해서 풀면 좋다.

n = 10
roads = [[1, 0],
         [1, 2],
         [8, 5],
         [9, 7],
         [5, 6],
         [5, 4],
         [4, 6],
         [6, 7]]


def solution(n, roads):
    day, prev = 1, []
    res = [-1] * n
    matrix = {i: set() for i in range(n)}

    for cityA, cityB in roads:
        matrix[cityA].add(cityB)
        matrix[cityB].add(cityA)
    print('map: ', matrix)

    while prev != res:
        prev = res[:]  # res를 복사 - 다른 변수로 등록된다. 그냥하면 안됨.
        print('situation:', prev)
        for i in range(n):
            # 순환을 찾기보다는 순환의 경우 어떠한 형식으로 노드를 가지고 있어야 하는지를 파악한다.
            # 만약 순환이라면, 1개이상의 노드를 가지고 있다.
            # 그리고 day를 통해서 노드가 1개의 길을 가진 노드들은 다 점령 상태( Visited)이기 때문에,
            # 여러 노드를 검사했을때, 주어진 조건을 성립하는 곳은 순환하는 곳만 남게 된다.
            if res[i] == -1 and len({a for a in matrix[i] if res[a] in [-1, day]}) <= 1:
                print(i, 'city conquer', day, 'days')
                res[i] = day

        day += 1

    return res


print(solution(n, roads))
