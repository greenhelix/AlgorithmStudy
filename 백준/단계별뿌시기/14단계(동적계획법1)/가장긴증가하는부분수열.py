# https://www.acmicpc.net/problem/11053
n = int(input())
s = list(map(int, input().split()))
dp = [0]*n
# print(n, s, dp)

for i in range(0, n):
    m = 0
    for j in range(i):
        if s[i] > s[j]:
            m = max(m, dp[j])
    dp[i] = m + 1

print(max(dp))
