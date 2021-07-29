# https://www.acmicpc.net/problem/15649
# n,m - 1~n 까지 m개의 수열종류를 리턴하라 # 백트래킹
import sys
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
        print(result)
        result.pop()
        checker[i] = False


dfs(0)
