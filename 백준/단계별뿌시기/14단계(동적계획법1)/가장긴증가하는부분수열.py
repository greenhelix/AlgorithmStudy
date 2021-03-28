# https://www.acmicpc.net/problem/11053
# LIS - 최장 증가 부분수열 문제이다. (https://namu.wiki/w/%EC%B5%9C%EC%9E%A5%20%EC%A6%9D%EA%B0%80%20%EB%B6%80%EB%B6%84%20%EC%88%98%EC%97%B4)

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
