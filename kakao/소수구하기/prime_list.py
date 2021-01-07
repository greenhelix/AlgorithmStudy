import math
# a~b범위 안에 소수들의 합을 구한다.


def primesSum(a, b):
    return sum(filter(lambda x: all(x % i for i in range(2, int(math.sqrt(x)) + 1)), range(max(2, a), b + 1)))
# int(math.sqrt(x)) --> = 같은 표현이다. == > int(x**0.5)
# 에라토스테네스의 체 구현.


def prime_list(n):
    show = [True] * (n + 1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if show[i] == True:
            for j in range(i + i, n, i):
                show[j] = False
    return [i for i in range(2, n + 1) if show[i] == True]

# 원리는 비슷하다. 범위 내에 True, False를 통해 배수가 있느지 없는지 확인
# 조건에 충족하면 소수로 본다. 제곱근을 통해서 범위내에 배수 여부를 확인해주는 것이 포인트이다.
