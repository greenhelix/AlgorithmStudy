# https://www.acmicpc.net/problem/10430
# 수학
a, b, c = input().split()
d = (int(a) + int(b)) % int(c)
e = (int(a) * int(b)) % int(c)
print(d)
print(d % int(c))
print(e)
print(e % int(c))
