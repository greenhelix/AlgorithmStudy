# https://www.acmicpc.net/problem/3053
from math import pi
r = int(input())
# uclid pi * (r**2) , taxi |x1-x2| - |y1-y2|
uclid, taxi = pi * (r ** 2), 2*(r**2)
print(f'{uclid:.6f}\n{taxi:.6f}')  # 소수점 6자리 나타내는 방법
