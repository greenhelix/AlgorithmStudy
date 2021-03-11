class Prizes(object):
    def __new__(_, p, n, d):
        return [(i+1)*n for i, v in enumerate(p[n-1::n]) if v % d == 0]


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
