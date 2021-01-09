# https: // www.acmicpc.net / problem / 11021
# 구현 / 수학 / 사칙연산
T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    print(f'Case #{i+1}: {a+b}')
