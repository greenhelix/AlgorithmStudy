class Prizes(object):
    def __init__(self, purchases, n, d):
        self.purchases = purchases
        self.n = n
        self.d = d

    def __iter__(self):
        for i in range(self.n - 1, len(self.purchases), self.n):
            if self.purchases[i] % self.d == 0:
                yield i + 1


def superPrize(purchases, n, d):
    return list(Prizes(purchases, n, d))
