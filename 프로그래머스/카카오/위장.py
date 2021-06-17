from functools import reduce
from collections import Counter


def solution(clothes):
    return reduce(lambda x, y: x * y, [(i + 1) for i in Counter([j[1] for j in clothes]).values()]) - 1


clothes = [["yellowhat", "headgear"], [
    "bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))
