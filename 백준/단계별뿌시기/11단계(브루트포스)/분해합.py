# https://www.acmicpc.net/problem/2231
# 브루트포스 알고리즘
# 어떤 자연수 N이 있을 때, 그 자연수 N의 분해합은 N과 N을 이루는 각 자리수의 합을 의미한다.
# 어떤 자연수 M의 분해합이 N인 경우, M을 N의 생성자라 한다.
# 예를 들어, 245의 분해합은 256(=245+2+4+5)이 된다. 따라서 245는 256의 생성자가 된다. 물론, 어떤 자연수의 경우에는 생성자가 없을 수도 있다.
# 반대로, 생성자가 여러 개인 자연수도 있을 수 있다.
# 자연수 N이 주어졌을 때, N의 가장 작은 생성자를 구해내는 프로그램을 작성하시오.
# 첫째 줄에 자연수 N(1 ≤ N ≤ 1,000,000)이 주어진다.
# 216
''' 브루투포스 알고리즘은 무식하게 실행시키면된다.'''
N = int(input())  # Str로 받는다.
# # x + (x의각자릿수의합) == n 이면 생성자가된다.
# print(list(N), len(N))  # 리스트화 시킨다.

# n = int(N)
# # 범위 111 ~ 999
# start = int('1' * len(N))  # 111
# end = int('9' * len(N))  # 999
# if n == 0:
#     print(0)

# for i in range(start, end + 1):
#     temp = list(str(i))
#     합 = sum(int(i) for i in temp)
#     if n == (i + 합):
#         print(i)
#         break

# == == == == == == == == =
num = 0
for i in range(1, N + 1):
    divide = list(map(int, str(i)))
    ssum = i + sum(divide)
    if ssum == N:
        num = i
        break
print(num)
