# https: // www.acmicpc.net / problem / 2439
# 구현
T = int(input())
for i in range(1, T+1):
    print(f'{" "*(T-i)}{"*"*i}')
