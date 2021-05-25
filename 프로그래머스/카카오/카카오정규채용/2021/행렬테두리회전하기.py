# https://programmers.co.kr/learn/courses/30/lessons/77485
'''
이 행렬에서 직사각형 모양의 범위를 여러 번 선택해, 테두리 부분에 있는 숫자들을 시계방향으로 회전시키려 합니다.
각 회전은 (x1, y1, x2, y2)인 정수 4개로 표현
x1 행 y1 열부터 x2 행 y2 열까지의 영역에 해당하는 직사각형에서 테두리에 있는 숫자들을 한 칸씩 시계방향으로 회전.
회전들의 목록 queries
세로 길이(행 개수) rows, 가로 길이(열 개수) columns
각 회전들을 배열에 적용
그 회전에 의해 위치가 바뀐 숫자들 중 가장 작은 숫자들을 순서대로 배열에 담아 return 하도록 solution 함수를 완성
'''
r = 6
c = 6
query = [[2, 2, 5, 4], [3, 3, 6, 6], [5, 1, 6, 3]]


def solution(rows, columns, queries):
    answer = []
    matrix = [[] for _ in range(rows)]

    for i in range(1, rows+1):
        for j in range(1, columns+1):
            matrix[i-1].append((i-1)*columns + j)

    print('>>처음 행렬의 구성')
    print(*matrix, sep='\n')
    print()

    for x1, y1, x2, y2 in queries:
        m = 100001
        temp = matrix[x1 - 1][y2 - 1]
        print(temp)
        # 윗면
        m = min(min(matrix[x1 - 1][y1 - 1: y2 - 1]), m)
        matrix[x1 - 1][y1:y2] = matrix[x1 - 1][y1 - 1: y2 - 1]

        # 왼쪽
        for i in range(x1, x2):
            m = min(matrix[i][y1 - 1], m)
            matrix[i - 1][y1 - 1] = matrix[i][y1 - 1]

        # 아랫면
        m = min(min(matrix[x2 - 1][y1:y2]), m)
        matrix[x2 - 1][y1 - 1: y2 - 1] = matrix[x2 - 1][y1:y2]

        # 오른쪽
        for i in range(x2 - 2, x1 - 2, -1):
            m = min(matrix[i][y2 - 1], m)
            matrix[i + 1][y2 - 1] = matrix[i][y2 - 1]

        matrix[x1][y2 - 1] = temp
        m = min(m, temp)

        answer.append(m)

    return answer


# def rotate(query, matrix):
#     m = 0
#     temp = dict()
#     # [2, 2, 5, 4] -> [1, 1, 4, 3]
#     x1, y1, x2, y2 = map(lambda x: x-1, query)
#     print(f'query{list(query)}에 -1을 반영-->{x1, y1, x2, y2}')
#     print()
#     print('>>>회전 전 행렬')
#     print(*matrix, sep='\n')
#     print()
#     for x in range(x1, x2+1):
#         for y in range(y1, y2 + 1):
#             if x in [x1, x2] or y in [y1, y2]:
#                 temp[matrix[x][y]] = [x, y]

#                 if x == x1 and y < y2:  # 오른쪽
#                     temp[matrix[x][y]] = [x, y+1]
#                 elif x == x2 and y > y1:  # 왼쪽
#                     temp[matrix[x][y]] = [x, y-1]
#                 elif x < x2 and y == y2:  # 아래
#                     temp[matrix[x][y]] = [x+1, y]
#                 elif x > x1 and y == y1:  # 위
#                     temp[matrix[x][y]] = [x-1, y]

#     print(temp, '\n')
#     m = min(temp.keys())  # 회전 부분의 최소값을 저장

#     # 각 변한 x,y의 인덱스를 matrix에 반영한다.
#     for k, v in temp.items():
#         matrix[v[0]][v[1]] = k
#     print()

#     return matrix, m


print(solution(r, c, query))
