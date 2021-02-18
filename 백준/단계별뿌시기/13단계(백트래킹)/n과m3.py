# https://www.acmicpc.net/problem/15651
import sys
n, m = map(int, sys.stdin.readline().split())
arr = range(1, n + 1)
visited = [0] * n
result = [0] * m


def dfs(n, m, k):
    if n == k:
        print(*result)
        return
    else:
        for i in range(m):
            visited[i] = 1
            result[n] = arr[i]
            dfs(n + 1, m, k)
            visited[i] = 0


dfs(0, n, m)
