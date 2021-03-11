def getPoints(answers, p):
    def questionPoints(x, y): return x+1 if y == 1 else -p
    res = 0
    for i, ans in enumerate(answers):
        res += questionPoints(i, ans)
    return res


sample = [True, True, False, True]
p = 2
print(getPoints(sample, p))
