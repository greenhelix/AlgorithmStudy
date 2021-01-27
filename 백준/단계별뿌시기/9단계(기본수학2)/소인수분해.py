# https://www.acmicpc.net/problem/11653
# n = int(input())
# num = []
# for i in range(1, n + 1):
#     count = 0
#     for j in range(1, i + 1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         num.append(i)
# print(num)  # 소수를 모아둔다.

# if n == 1:
#     print()
# else:
#     result = []
#     while n != 1:
#         for i in num:
#             if n % i == 0:
#                 n = n // i
#                 result.append(i)

#     # print(result)
#     print(*sorted(result), sep='\n')

n = int(input())
i = 2
while n != 1:
    if n % i == 0:
        n = n / i
        print(i)
    else:
        i += 1
