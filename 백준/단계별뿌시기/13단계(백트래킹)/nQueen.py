# https://www.acmicpc.net/problem/9663
# 대표적인 백트래킹 문제 이다.
n = int(input())
row = [0 for i in range(16)]
result = 0


def isTrue(x):
    for i in range(1, x):
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(cnt):
    global result
    if cnt > n:
        result += 1
    else:
        for i in range(1, n + 1):
            row[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)


dfs(1)
print(result)
