# https://www.acmicpc.net/problem/2581
m = int(input())
n = int(input())
# m 이상 n 이하 자연수 중 소수인 것을 모두 골라 이들 소수의 합, 최솟값을 찾아라.
result = []
for i in range(m, n + 1):
    count = 0
    for j in range(1, i + 1):
        if i % j == 0:
            count += 1
    if count == 2:
        result.append(i)

if len(result) == 0:
    print(-1)
else:
    print(sum(result))
    print(min(result))
