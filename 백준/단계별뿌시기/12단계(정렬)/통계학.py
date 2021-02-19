# https://www.acmicpc.net/problem/2108
from collections import Counter
import sys
n = int(sys.stdin.readline())
number = [int(sys.stdin.readline()) for i in range(n)]

# print(number)

# 평균
avr = 0
for i in number:
    avr += i

print(avr // n)


# 중앙값(인덱스상에서 중)
number.sort()
# print(number)
print(number[n // 2])

# 최빈값
# print(number)
counting = Counter(number)
# print(counting)
show_num = counting.most_common()
# print(show_num)

if len(number) > 1:
    if show_num[0][1] == show_num[1][1]:
        print(show_num[1][0])
    else:
        print(show_num[0][0])
else:
    print(show_num[0][0])

# 범위출력
print(max(number) - min(number))
