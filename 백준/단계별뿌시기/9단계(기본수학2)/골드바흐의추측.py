# https://www.acmicpc.net/problem/9020
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


for i in range(n):
    print(i+1, 'case')
    a = int(input())
    print(a, 'input..')
    middle = aristo(a)
    print('middle:', middle)
    temp = []
    for i in range(len(middle)):
        for j in range(len(middle)):
            if middle[i] + middle[j] == a:
                temp.append((middle[i], middle[j]))

    print('show all case...', temp)
