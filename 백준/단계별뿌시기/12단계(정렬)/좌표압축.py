# https://www.acmicpc.net/problem/18870
# import sys
# input = sys.stdin.readline
# n = int(input())
# matrix = list(map(int, input().split()))
# count = [0]*n
# print(matrix, count)

# for i in range(n):
#     check = set()
#     for j in range(n):
#         if matrix[i] > matrix[j] and i != j:
#             check.add(matrix[j])
#         print(check, i, 'finish')
#         count[i] = len(check)
# print(count)

# 위의 방법은 시간초과 발생 정렬을 통해서 풀이해야한다.
n = int(input())
matrix = list(map(int, input().split()))  # 2 4 -10 4 -9
# 순위를 매겨본다.
grade = list(sorted(set(matrix)))
print(grade)  # [-10, -9, 2, 4] 낮은 수부터 정렬시킨다. 중복도 제거한다.
# 딕셔너리를 통해 해당 순위를 카운트해준다.
grade = {grade[i]: i for i in range(len(grade))}
print(grade)

print(*[grade[i] for i in matrix])
