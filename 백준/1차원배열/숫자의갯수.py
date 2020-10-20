# 백준 2577번 numpy 나 이런 라이브러리 쓰면 안됨.
a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
count = [0] * 10
for i in range(10):
    for j in range(len(d)):
        if i == int(d[j]):
            count[i] += 1
    print(count[i])
# import numpy
# a = [int(input()) for i in range(3)]
# # print(numpy.prod(a))
# b = str(numpy.prod(a))
# result = [0] * 10
# for i in range(10):
#     for j in range(len(b)):
#         if i == int(b[j]):
#             result[i] += 1
#     print(result[i])
