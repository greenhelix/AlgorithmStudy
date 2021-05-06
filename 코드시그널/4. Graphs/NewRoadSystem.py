from collections import defaultdict

sample = [
    [False, True, True, False],
    [True, False, True, False],
    [True, True, False, True],
    [False, False, True, False]
]
def ace_greatRenaming(roadRegister):
    swap = lambda x: [x[-1]] + x[:-1]
    return swap([swap(row) for row in roadRegister])

def greatRenaming(roadRegister):
    matrix = defaultdict(list)
# 형태는 그대로 유지하되 도시명만 i -> i+1로 바꾸고, 숫자가 가장큰 도시는 0으로 바꾼다.
# 이상태로 처음 등록되 도시관계도가 일치하게 만들어라
    m = len(roadRegister)-1
    answer = [[False] * (m+1) for _ in range(len(roadRegister))]
    for i in range(len(roadRegister)):
        for j in range(len(roadRegister[i])):
            if roadRegister[i][j] == True:
                if i == m:
                    print('i_max', i, j)
                    matrix[0].append(j+1)
                elif j == m:
                    print('j_max', i, j)
                    matrix[i+1].append(0)
                else:
                    matrix[i+1].append(j+1)

    # matrix = sorted(matrix.items())
    # print('matrix', matrix)

    for k, v in matrix.items():

        for i in v:
            if answer[k][i] == False:
                answer[k][i] = True

    return answer


print(greatRenaming(sample))
