# https://www.acmicpc.net/problem/1427
# 2143 -> 4321
n = list(map(int, input()))
print("".join(map(str, sorted(n, reverse=True))))
