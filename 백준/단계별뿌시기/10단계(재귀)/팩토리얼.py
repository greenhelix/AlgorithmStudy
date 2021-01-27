# https://www.acmicpc.net/problem/10872
n = int(input())


def fac(a):
    if a == 0 or a == 1:
        return 1
    else:
        return a * fac(a - 1)


print(fac(n))
