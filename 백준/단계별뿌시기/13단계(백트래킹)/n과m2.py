# https://www.acmicpc.net/problem/15650
import sys
n, m = map(int, sys.stdin.readline().split())

num_list = [i + 1 for i in range(n)]
checker = [False] * n
result = []


def dfs(s):
    if s == m:
        print(*result)
    for i in range(0, n):
        if checker[i]:
            continue
        checker[i] = True
        result.append(num_list[i])
        dfs(s + 1)
        result.pop()

        for j in range(i + 1, n):
            checker[j] = False


dfs(0)
