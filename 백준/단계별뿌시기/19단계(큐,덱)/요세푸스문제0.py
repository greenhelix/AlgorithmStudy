# https://www.acmicpc.net/problem/11866
from collections import deque
n, k = map(int, input().split())
numbers = deque(i for i in range(1, n + 1))

print('<', end='')
while numbers:
    for i in range(k - 1):
        numbers.append(numbers[0])
        numbers.popleft()
    print(numbers.popleft(), end='')

    if numbers:
        print(',', end=' ')
print('>')
