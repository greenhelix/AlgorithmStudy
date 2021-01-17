# https://www.acmicpc.net/problem/2775
# 수학 / 조합론
case = int(input())

for _ in range(case):
    층수 = int(input())
    호수 = int(input())
    층별인원 = [i for i in range(1, 호수 + 1)]
    for _ in range(층수):
        for j in range(1, 호수):
            층별인원[j] += 층별인원[j - 1]

    print(층별인원[-1])
# 내가 찾은 방법이지만, 틀렸다고 판명...
# for _ in range(case):
#     k = int(input())
#     n = int(input())
#     print((k+1)*n+(k-1))

# comb 수학에서 조합의 개념을 사용
# from math import comb
# num = int(input())
# for i in range(num):
#     k = int(input())
#     n = int(input())
#     print(f'{comb(k+n, n-1)}')
