# https://www.acmicpc.net/problem/10989
# 일반적인 정렬로는 안됨,
# 카운팅 정렬 알고리즘을 사용한다
# non-comparison sort algorithm
from collections import Counter
import sys
# 최대 범위를 알아야 움직이는 풀이이다.
n = int(sys.stdin.readline())
pot = [0] * 10001
for i in range(n):
    pot[int(sys.stdin.readline())] += 1

for i in range(10001):
    if pot[i] != 0:
        print('%s\n' % i * pot[i], end="")


# 메모리 초과 풀이 - 해결은 된다. Counter 활용
n = int(sys.stdin.readline())
a = []
c = [0] * n
for i in range(n):
    a.append(int(sys.stdin.readline()))

a = list(Counter(a).items())
a.sort()

for i in range(len(a)):
    for j in range(a[i][1]):
        print(a[i][0])
