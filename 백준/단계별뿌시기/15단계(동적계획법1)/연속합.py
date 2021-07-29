# https://www.acmicpc.net/problem/1912
n = int(input())
s = list(map(int, input().split()))
dp = [0 for _ in range(n)]
print(dp)
dp[0] = s[0]

for i in range(1, n):
    dp[i] = max(s[i], dp[i - 1] + s[i])

print(dp)
print(max(dp))
