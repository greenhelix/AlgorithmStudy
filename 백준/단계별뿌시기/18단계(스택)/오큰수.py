# https://www.acmicpc.net/problem/17298
# 메모리 제한 512MB  정답 비율 34%

# 크기가 n인 수열  a가 있다.
# 수열의 각 원소 a[i] 에 대해서 오큰수 NGE(i)를 구하려 한다.
# a[i] 의 오큰수 = 오른쪽에 있으면서 a[i]보다 큰 수 중에서 가장 왼쪽에 있는 수를 의미한다.
# 그러한 수가 없는 경우에는 a[i]의 오큰수 = -1 이다.

# 예시)
# a = [3, 5, 2, 7]
# NGE(1) = 5, NGE(2) = 7, NGE(3) = 7, NGE(4) = -1

# input1 -> a의 크기 n = (1<= n <= 1000000)
# input2 -> a의 원소 a[1], a[2], a[3]... a[n] 이 주어진다.

# output -> 총 n개의 수 NGE(1), NGE(2)...NGE(n) 을 공백으로 구분하여 출력한다.

# testcase input
# 4
# 3 5 2 7
# testcase output
# 5 7 7 -1


# 1차 시도 : 시간초과
# 2차 시도 : 시간초과 -1인 경우 필터링 추가
# from collections import deque
# global a
# n = int(input())
# a = deque(map(int, input().split()))
# print(n, a, type(a))  # 4 [3, 5, 2, 7]
# result = []
# def NGE(p, nums):
#     bigO = []
#     for i in range(len(nums)):
#         if p < nums[i]:
#             bigO.append(nums[i])
#     return bigO[0]
# while a:
#     point = a.popleft()
#     print(f'point:{point}, {a}')
#     if not a:
#         result.append(-1)
#         break
#     result.append(NGE(point, a))
# print(*result)

# 3차 시도 : 좀 더 유연한 스택활용을 했어야 했다.
n = int(input())
a = list(map(int, input().split()))

stack = []
result = [-1 for _ in range(n)]

stack.append(0)
i = 1

while stack and i < n:
    while stack and a[stack[-1]] < a[i]:
        result[stack[-1]] = a[i]
        stack.pop()
    stack.append(i)
    i += 1

print(*result)
