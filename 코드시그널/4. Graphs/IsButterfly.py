adj = [[False, True, True, False, False],
       [True, False, True, False, False],
       [True, True, True, True, True],
       [False, False, True, False, True],
       [False, False, True, True, False]]

# 5개의 노드가 주어진다. 이 노드들의 길을 연결했을때, 나비 모양인지 아닌지 확인한다.


def solution(roads):
    matrix = {i: set() for i in range(len(roads))}
    for i in range(len(roads)):  # 값을 넣어주어, 지도를 완성한다.
        for j in range(len(roads)):
            if roads[i][j]:
                matrix[i].add(j)
                matrix[j].add(i)

    print(matrix)
    mid = True
    for k, v in matrix.items():  # 중간 점을 찾아낸다.
        cnt = 0
        if len(v) == 4:

            print(k, 'is middle')
            mid = False

    if mid:
        print('no middle')
        return False

    confirm = 0
    for i in range(len(matrix)):  # 중간 점을 찾아낸 경우, 날개가 두짝인지 확인한다.
        for j in range(i + 1, len(matrix)):
            if len(matrix[i]) == 2 and len(matrix[j]) == 2:
                if [i, j] == sorted(matrix[i] ^ matrix[j]):
                    confirm += 1

    if confirm == 2:  # 두 날개 다 있으면 True를 리턴한다.
        print('two wings')
        return True
    print('adnormal wings')
    return False


print(solution(adj))
