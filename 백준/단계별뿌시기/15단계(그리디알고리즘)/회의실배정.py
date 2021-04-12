# https://www.acmicpc.net/problem/1931
# 한개의 회의실 사용하고자할 n개의 회의
# 이에 따라 회의실 사용표 제작.
# 시작-끝 시간 , 겹치지 않게 사용할 수 있는 회의 최대 갯수
# 시작-끝 같을 수 있다. 시작하자마자 끝나는 경우도 있음.

n = int(input())
matrix = []

for _ in range(n):
    matrix.append(tuple(map(int, input().split())))

matrix = sorted(matrix, key=lambda x: (x[1], x[0]))

last, count = 0, 0
for i, j in matrix:
    if i >= last:
        count += 1
        last = j

print(count)

# 하나의 회의 시간을 고른다.- 제일 작은 값 부터 하기 위해선 정렬을 해준다.

# 시작 시간의 시퀀스를 확인 - 통과?
# 해당 회의의 종료 시간이 다음 시작 시간보다 작은지 확인 - 통과?

# 두 가지경우를 충족하면 해당 회의를 카운트를 해준다.


# def check(c):
#     count = [c]
#     for i in range(n):
#         print('now check', c)
#         if c[0] < matrix[i][0]:
#             print('first success', c, matrix[i])
#             if c[1] < matrix[i][0]:
#                 print('second success!', c, matrix[i], '\n')
#                 count.append(matrix[i])
#                 c = matrix[i]
#     print('final', count)
#     return len(count)


# find = []
# for i in matrix:
#     find.append(check(i))

# print(find)
# print(max(find))
