# https://www.acmicpc.net/problem/15649
# n,m - 1~n 까지 m개의 수열종류를 리턴하라 # 백트래킹
import sys
temp = []
n, m = map(int, sys.stdin.readline().split())

num_list = [i + 1 for i in range(n)]
checker = [False] * n
result = []


def dfs(s):
    if s == m:
        print(*result)
        return
    for i in range(0, n):
        if checker[i]:
            continue

        checker[i] = True
        result.append(num_list[i])

        dfs(s + 1)

        result.pop()
        print(result)
        print(checker)
        checker[i] = False


dfs(0)

# def fac(a) -> int:
#     re = 1
#     while a != 0:
#         re *= a
#         a -= 1
#     return re


# size = int(fac(n) / fac(m))
# re = [[0]*m] * size
# print(re)
# print(*re, sep='\n')
# test = set()
# test.add('123')
# test.add('123')
# test.add('122')
# print(test)
# for i in test:
#     print(i)
