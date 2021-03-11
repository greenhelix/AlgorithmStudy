def listConcatenation(lst1, lst2):
    res = lst1
    res.extend(lst2)
    return res


l1 = [2, 2, 1]
l2 = [10, 11]
print(list(zip(l1, l2)))
print(listConcatenation(l1, l2))
