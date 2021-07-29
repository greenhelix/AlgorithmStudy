# https://www.acmicpc.net/problem/15652
n, m = map(int, input().split())
number = [i + 1 for i in range(n)]

checker = [False] * n
result = []


def dfs(s):
    if s == m:
        print(*result)
        return

    for i in range(0, n):
        if checker[i]:
            continue
        result.append(number[i])
        dfs(s + 1)
        checker[i] = True
        result.pop()

        for j in range(i + 1, n):
            checker[j] = False


dfs(0)
