# https://www.acmicpc.net/problem/7568
# n = int(input())
# weight, heihgt = [], []
# for i in range(n):
#     x, y = map(int, input().split())
#     weight.append(x)
#     heihgt.append(y)
# print(weight, heihgt)
# temp = [[0]*n for _ in range(2)]
# result = [0]*n
# def whoIsBig(w, h):
#     for i in range(len(w)):
#         if w[0] == w[i]:
#             temp[0][i] = 0
#         elif w[0] > w[i]:
#             temp[0][i] = -1
#         elif w[0] < w[i]:
#             temp[0][i] = 1
#     for i in range(len(h)):
#         if h[0] == h[i]:
#             temp[1][i] = 0
#         elif h[0] > h[i]:
#             temp[1][i] = -1
#         elif h[0] < h[i]:
#             temp[1][i] = 1
#     return temp
# whoIsBig(weight, heihgt)
# print(temp)
# for i in range(n):
#     result[i] = temp[0][i] + temp[1][i]
# print(result)
# m = max(result)
# count = 0
# for i in range(n):
#     if m == result[i]:
#         result[i] = 1
#         count += 1


# 브루트포스 완전탐색
n = int(input())
people = []
for _ in range(n):
    weight, heihgt = map(int, input().split())
    people.append((weight, heihgt))
for i in people:
    rank = 1
    for j in people:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")
