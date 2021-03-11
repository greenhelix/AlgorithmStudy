def mexFuntion(s, upperBound):
    found = -1
    for i in range(upperBound):
        if not i in s:
            found = i
            break
    else:
        found = upperBound
    return found


s = [0, 4, 2, 3, 1, 7]
upperBound = 10
print(mexFuntion(s, 10))
