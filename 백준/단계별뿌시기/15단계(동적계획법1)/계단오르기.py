# https://www.acmicpc.net/problem/2579
# 내생각으로는 깊이탐색을 통해서 각 루트를 저장하며, 최종 합산 점수를 추출해내고
# 주어진 조건, 연속 두번만 가능하며, 최종 칸의 값은 마지막 칸이 딱 떨어져야한다.
# 이러한 점을 봤을 때 루트대로 따로 뽑고, 최종합산 점수를 리스트화 해서
# 그 중에서 최대값을 추출하는 것으로 생각했다.

n = int(input())
s = [0 for i in range(301)]
dp = [0 for i in range(301)]
for i in range(n):
    s[i] = int(input())
dp[0] = s[0]
dp[1] = s[0] + s[1]
dp[2] = max(s[1] + s[2], s[0] + s[2])
for i in range(3, n):
    dp[i] = max(dp[i - 3] + s[i - 1] + s[i], dp[i - 2] + s[i])
print(dp[n - 1])
