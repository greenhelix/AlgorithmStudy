# https://www.acmicpc.net/problem/2630
# 메모리 제한 : 128MB , 정답비율 : 70.772%

# 전체종이 n*n (n = 2의k승, 1<=k<=7 자연수)
# 종이를 자르는 규칙
# 1. if 모든 같은 색이 아니다? -> 중앙부분을 잘라서 4등분 한다.
# 2. 각 조각 별로 1번 반복
# 3. 조작이 모두 같은 색이다? -> 자르기 멈춘다.

# input1 : n의 값 (2, 4, 8, 16, 32, 64, 128 중 하나다.)
# input2 : 종이에 색칠 된 정보 - 0 = white, 1 = blue
# ouput : 하얀색 색종이, 파란색 색종이 갯수 구하기

# input
# 8
# 1 1 0 0 0 0 1 1
# 1 1 0 0 0 0 1 1
# 0 0 0 0 1 1 0 0
# 0 0 0 0 1 1 0 0
# 1 0 0 0 1 1 1 1
# 0 1 0 0 1 1 1 1
# 0 0 1 1 1 1 1 1
# 0 0 1 1 1 1 1 1

# ouput
# 9
# 7

n = int(input())
global matrix
matrix = [list(map(int, input().split())) for _ in range(n)]
# print(*matrix, sep='\n')
blue, white = 0, 0
test = [[] for _ in range(4)]


def check(paper):
    temp = 0

    for i in range(len(paper)):
        temp += sum(paper[i])
        print('temp:', temp, i)
        if sum(paper[i]) != len(paper) and sum(paper[i]) > 0:
            return 'slice'

    if temp == 0:
        return 'white'
    elif temp == len(paper) ** 2:
        return 'blue'
    else:
        return 'slice'


def slice(paper):
    slice_paper = [[] for _ in range(4)]
    l = len(paper) // 2
    case = [(0, 0), (0, l), (l, 0), (l, l)]
    cnt = 4
    while cnt > 0:
        for i in range(len(l)):
            for j in range(len(l)):

                # slice_paper[1] =
                # slice_paper[2] =
                # slice_paper[3] =

    return slice_paper


result = check(matrix)


if result == 'slice':
    print('slice do it!')

elif result == 'blue':
    blue = 1
elif result == 'white':
    white = 1
print('slice!!>>', slice(matrix))

# Final Print Section
print(f'white: {white}\nblue: {blue}')
