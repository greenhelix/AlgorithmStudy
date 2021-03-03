# https://www.acmicpc.net/problem/4948


def aristo(a, b):
    count = 0
    re = []
    b += 1
    show = [True] * b
    for i in range(2, int(b ** 0.5) + 1):
        if show[i]:
            for j in range(2 * i, b, i):
                show[j] = False
    for i in range(a+1, b):
        if i > 1 and show[i] == True:
            count += 1
            re.append(i)

    return re


while True:
    a = int(input())
    if a == 0:
        break
    print(aristo(a, 2 * a))
