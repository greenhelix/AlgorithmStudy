# https://www.acmicpc.net/problem/5431

# t <= 100
from sys import stdin
from collections import deque
read = stdin.readline
t = int(read())
# print('t = ', t)
books = deque()


def check(l):
    count = 0
    while list(l) != sorted(l):
        for i in range(len(l) - 1):
            if l[i] > l[i + 1]:
                temp = l[i + 1]
                del l[i + 1]
                l.appendleft(temp)
                count += 1
                # print(l)
                break
    return count


for test in range(t):
    n = int(read())
    # print(f'{test+1}test N = {n}')
    books = deque(map(int, read().split()))
    # print(f'books= {books}')
    # 오름차순으로 정렬
    print(f'result = {check(books)}')
    print(list(books), sorted(books))
    print('=====')
