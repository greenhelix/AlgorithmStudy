# https://www.acmicpc.net/problem/10870
# from sys import stdin
# n = int(stdin.readline())
# # 0<= n <= 20
# fibo = [0] * 20
# fibo[0], fibo[1] = 0, 1

# if n >= 2:
#     for i in range(2, n+1):
#         fibo[i] = fibo[i - 1] + fibo[i - 2]
# elif n == 1:
#     print(fibo[1])
# elif n == 0:
#     print(fibo[0])

# print(fibo[n])

# 재귀 형식으로 풀어야함.!!
def fibo(num):
    if num <= 1:
        return num
    return fibo(num - 1) + fibo(num - 2)


n = int(input())
print(fibo(n))
