# https://www.acmicpc.net/problem/1110
# 수학 / 구현
n = input()
one = n
cycle = 0
while True:
    # print('n:', one)
    cy = str(sum(map(int, n)))
    # print('sum:', cy)
    temp = n[-1] + cy[-1]
    # print('new n:', temp)
    n = temp
    cycle += 1
    if int(one) == int(n):
        print(cycle)
        break
