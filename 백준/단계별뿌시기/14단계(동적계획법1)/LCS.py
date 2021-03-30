# https://www.acmicpc.net/problem/9251
# LCS(Longest Common Subsequence, 최장 공통 부분 수열)문제는 두 수열이 주어졌을 때,
# 모두의 부분 수열이 되는 수열 중 가장 긴 것을 찾는 문제이다.
# 예를 들어, ACAYKP와 CAPCAK의 LCS는 ACAK가 된다.

# 문자열을 리스트로 받는다.
a = [x for x in input()]
b = [x for x in input()]
aLen, bLen = len(a), len(b)
# 한칸씩 늘려서, 기억할 공간을 만들어둔다.
dp = [[0] * (aLen + 1) for _ in range(bLen + 1)]

for i in range(1, bLen + 1):
    for j in range(1, aLen + 1):
        dp[i][j] = max(dp[i][j - 1], dp[i - 1][j], dp[i - 1]
                       [j - 1] + (a[j - 1] == b[i - 1]))

print(dp[bLen][aLen])
