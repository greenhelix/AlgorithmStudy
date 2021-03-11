class Prizes(object):
    def __init__(self, p, n, d):
        self.p = p
        self.n = n
        self.d = d
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            self.count += 1
            now = self.n
            if now * self.count > len(self.p):
                raise StopIteration
            elif self.p[now * self.count - 1] % self.d == 0:
                return self.n * self.count


def superPrize(purchase, n, d):
    return list(Prizes(purchase, n, d))


purchase = [12, 43, 13, 465, 1, 13]
n = 2
d = 3

print(superPrize(purchase, n, d))
