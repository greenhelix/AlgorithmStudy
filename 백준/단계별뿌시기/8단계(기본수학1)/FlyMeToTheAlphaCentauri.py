# https://www.acmicpc.net/problem/1011

# 제곱수, 제곱근등을 활용하여 규칙을 반영하여 패턴을 확인한 뒤
# 조건문을 통해서 걸러준다.
case = int(input())
for _ in range(case):
    x, y = map(int, input().split())
    gap = y - x
    num = 1
    while True:
        if num ** 2 <= gap < (num + 1) ** 2:
            break
        num += 1

    if num ** 2 == gap:
        print(num * 2 - 1)
    elif num ** 2 < gap <= num ** 2 + num:
        print(num * 2)
    else:
        print(num * 2 + 1)

# 마지막 움직임 1은 그냥 while문을 나오면서 자동 카운트되게 한다.
t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    distance = y - x
    count, move, now = 0, 1, 0
    while now < distance:
        count += 1
        now += move
        if count % 2 == 0:
            move += 1

    print(count)
