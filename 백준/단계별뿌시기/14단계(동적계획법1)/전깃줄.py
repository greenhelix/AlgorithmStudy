# https://www.acmicpc.net/problem/2565
# LIS 최장 증가 부분수열 문제로서, 해당 전깃줄의 순서를 Sorted를 통해서
# 정리해준다. 이상태로, 2번째 인자값을 기준으로 최장 증가 부분 수열이 되는
# 조건을 찾아준다. 즉, 최장 부분수열값을 찾아낸뒤 그 값을 해당 줄의 수 n
# 에서 빼주면 , 최소로 선을 제거해야할 수 가 나온다.
n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
matrix = sorted(matrix, key=lambda x: x[0])
dp = [0]*n
dp[0] = 1  # 이부분을 1로 안해주면 계속 틀리게 나온다. 주의.

for i in range(1, n):
    m = 0
    for j in range(i):
        if matrix[i][1] > matrix[j][1]:
            m = max(m, dp[j])
    dp[i] = m + 1

print(n - max(dp))
