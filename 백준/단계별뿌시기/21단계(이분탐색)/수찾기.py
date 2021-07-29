# https://www.acmicpc.net/problem/1920
# 이분탐색은 탐색부분을 둘로 분할하여 범위를 계속 줄여가는 방식이다.
# 속도가 더 빨라진다.
# 1. 정렬
# 2. 범위x에서 최소값, 최대값을 잡아주고
# 3. 해당 최소, 최대의 중앙값을 구해준다.
# 4. 중앙값이 찾는 숫자인지 확인하여 범위를 좀혀준다.
# 5. 다시 해당 범위에서 최소, 최대값을 설정하고 구해주면된다.
# n = int(input())
# a = list(map(int, input().split()))
# m = int(input())
# b = list(map(int, input().split()))

# a.sort()


# def divide(num):
#     find = True
#     if a[n // 2] < num:
#         # print('중간보다 크다')
#         for i in range(n // 2, n):
#             if num == a[i]:
#                 print(1)
#                 find = False
#                 break
#         if find:
#             print(0)
#     else:
#         # print('중간보다 작다')
#         for i in range(0, n // 2 + 1):
#             if num == a[i]:
#                 print(1)
#                 break
#         if not find:
#             print(0)
#     return 0


# for i in range(m):
#     # print(b[i], '찾아볼까요')
#     divide(b[i])


from sys import stdin, stdout
n = stdin.readline()
A = sorted(map(int, stdin.readline().split()))
m = stdin.readline()
B = map(int, stdin.readline().split())


def divide(finding, A, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2    # 중앙값 인덱스를 찾아둔다.
    if finding == A[mid]:       # 중앙값과 찾는 것이 같다면 바로 1 리턴
        return 1
    elif finding < A[mid]:      # 중앙값보다 작다면, 시작, 끝을 다시 설정하여 재귀
        return divide(finding, A, start, mid - 1)
    else:
        return divide(finding, A, mid + 1, end)


for find in B:
    # 시작, 끝 값을 인덱스로 설정하여 시작하게 만든다.
    start = 0
    end = len(A) - 1
    print(divide(find, A, start, end))
