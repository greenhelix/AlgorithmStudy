from functools import partial
# partial 은 부분집합을 의미하는데, 주어진 함수를 적용하고 들어가는
# 파라미터 값에 변동이 필요할 때 사용한다. 함수를 두개 겹쳐놓는데,
# 부분함수 같이 사용한다고 보면된다.


def line_y(m, b, x):
    return m * x + b


def twoLines(line1, line2, l, r):
    line1_y = partial(line_y, line1[0], line1[1])
    line2_y = partial(line_y, line2[0], line2[1])
    balance = 0
    for x in range(l, r + 1):
        y1 = line1_y(x)
        y2 = line2_y(x)
        if y1 > y2:
            balance += 1
        elif y1 < y2:
            balance -= 1
    if balance > 0:
        return "first"
    if balance < 0:
        return "second"
    return "any"


c11 = [1, 2]
c12 = [2, 1]
l1 = 0
r1 = 2
print(twoLines(c11, c12, l1, r1), '!!!!')
