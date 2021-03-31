# https://www.acmicpc.net/problem/12865
n, k = list(map(int, input().split()))
wv = [list(map(int, input().split())) for _ in range(n)]

weight = [ele[0] for ele in wv]
values = [ele[1] for ele in wv]
dp = [[0 for _ in range(k + 1)] for _ in range(n+1)]

for i in range(1, n + 1):
    for j in range(1, k + 1):
        w = weight[i-1]
        v = values[i-1]
        if(j < w):
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(v + dp[i - 1][j - w], dp[i - 1][j])

print(dp[n][k])
