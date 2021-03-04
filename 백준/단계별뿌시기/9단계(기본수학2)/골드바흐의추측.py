# https://www.acmicpc.net/problem/9020
import time
start = time.time()
n = int(input())


def aristo(num):
    re = []
    num += 1
    checker = [True] * num
    for i in range(2, int(num ** 0.5) + 1):
        if checker[i]:
            for j in range(i * 2, num, i):
                checker[j] = False
    for i in range(0, num):
        if i > 1 and checker[i] == True:
            re.append(i)
    return re


def find(p, num):
    temp, case = [], []
    half = max([i for i in range(len(p)) if p[i] <= num/2])
    for i in range(half, -1, -1):
        for j in range(i, len(p)):
            if p[i] + p[j] == a:
                return [p[i], p[j]]


for i in range(n):
    a = int(input())
    m = aristo(a)
    print(" ".join(map(str, find(m, a))))
    
print(time.time() - start, 'time')