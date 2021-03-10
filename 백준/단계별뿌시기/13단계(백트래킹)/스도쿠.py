# https://www.acmicpc.net/problem/2580
# 0이 빈칸으로 인식하고, 정답 스도쿠를 출력하라
# 0 3 5 4 6 9 2 7 8
# 7 8 2 1 0 5 6 0 9
# 0 6 0 2 7 8 1 3 5
# 3 2 1 0 4 6 8 9 7
# 8 0 4 9 1 3 5 0 6
# 5 9 6 8 2 0 4 1 3
# 9 1 7 6 5 2 0 8 0
# 6 0 3 7 0 1 9 5 2
# 2 5 8 3 9 4 7 6 0
matrix = []

for _ in range(9):
    matrix.append(list(map(int, input().split())))
print('-----------------------------')
# 비어있는 자리, 0의 값인 부분의 좌표들을 쫘악 가져온다.
empty = [(i, j) for i in range(9) for j in range(9) if matrix[i][j] == 0]

for i in matrix:
    print(*i)

print('-----------------------------')


def isitFill(i, j):
    a, b = i, j
    cases = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    print('행과 종 검사 시작합니다.')
    for target in range(9):
        # 행검사
        if matrix[i][target] in cases:
            cases.remove(matrix[i][target])
        # 종검사
        if matrix[target][j] in cases:
            cases.remove(matrix[target][j])
    # 3*3큐브 검사
    print('행과 종 검사 완료*********************\n')
    print(f'좌표({i},{j}) 해당 위치 큐브 검사 시작합니다.')

    # 큐브의 해당 구간 시작점으로 조정해준다.
    i //= 3
    j //= 3
    print(f'좌표({a},{b})를 ({i},{j})로 변경')
    for p in range(i * 3, (i + 1) * 3):
        for q in range(j * 3, (j + 1) * 3):
            if matrix[p][q] in cases:
                cases.remove(matrix[p][q])

    print(f'좌표({a},{b}) 위치에는 {cases[0]}이 들어가야 합니다.\n')
    return cases  # 완료하면, 비어있는 칸을 찾아서 리턴한다. 해당 i, j위치에서


flag = False


def dfs(x):
    global flag
    if flag:
        return print('already perfect!!')
    if x == len(empty):  # 비어있는 칸의 맨 마지막 값이 되었을때, 값을 출력해준다.
        print('------------Answer-----------------')
        for row in matrix:
            print(*row)  # 각 줄을 출력해준다.

        flag = True  # 플래그를 올리고 리턴하여 종료한다.
        return print('complete!!')
    else:
        (i, j) = empty[x]  # 0으로 값이 없는 곳을 하나씩 넣어준다.
        cases = isitFill(i, j)  # 행,열, 큐브 탐색을 진행해서, 비어있는 곳의 값을 찾는다.

        for num in cases:
            matrix[i][j] = num  # 찾은 값을 스도쿠 안에 적는다.
            dfs(x + 1)  # 재귀형태로, 다음 빈칸을 찾아서 탐색을 시작한다.
            matrix[i][j] = 0  # 초기화해준다. (정답이 없을 경우를 대비)


dfs(0)
