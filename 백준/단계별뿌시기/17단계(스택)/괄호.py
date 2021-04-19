# https://www.acmicpc.net/problem/9012
a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:  # 균형이 애초에 안맞은 경우 바로 컷
            print('NO1')
            break
    if sum > 0:  # 최종적으로 뭔가가 하나더 있다면 컷
        print('NO2')
    elif sum == 0:
        print('YES')
