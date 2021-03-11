def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        res = res[1:-1]
        res = res
    return res


sample = [3, 4, 2, 4, 38, 4, 5, 3, 2]
print(listBeautifier(sample))
