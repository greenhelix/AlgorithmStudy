# https://www.acmicpc.net/problem/10871
# 수학/ 구현
N, X = map(int, input().split())
A = [int(a) for a in input().split()]
for i in range(N):
    if A[i] < X:
        print(f'{A[i]} ', end='')
