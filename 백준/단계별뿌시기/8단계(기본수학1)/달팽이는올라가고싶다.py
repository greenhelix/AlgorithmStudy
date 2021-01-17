# https://www.acmicpc.net/problem/2869
# 수학
a, b, v = map(int, input().split())
print(a, b, v)
# day, sun, night = 0, 0, 0
# while v > 0:
#     day += 1
#     sun = v - a
#     if sun <= 0:
#         break
#     night = sun + b
#     v = night
# print(day)
# 시간초과 발생되므로 수학적으로 접근해서 풀어야 한다.
# 원래 식은 (a * day) - (b * (day -1)) >= v 이다. 이것을 간단하게 day 로 치환하면, day >= (v-b)/(a-b) 가된다.
# 여기서 이 값이 float형태로 나올 수 있고, 소수점이 있는 값이 나올 수도 있다. 이러한 경우를 대비하여 if문을 통해서 4.1day 는 5 day 로 치환해주면된다.
day = (v - b) / (a - b)
print(int(day) if day == int(day) else int(day)+1)
