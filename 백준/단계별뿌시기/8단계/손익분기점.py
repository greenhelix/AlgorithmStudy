A, B, C = input().split()


def check(a, b, c):
    if (int(c) - int(b) == 0):
        return print('-1')
    result = int(int(a) / (int(c) - int(b)) + 1)
    if (result > 0):
        return print(str(result))
    else:
        return print('-1')


check(A, B, C)
