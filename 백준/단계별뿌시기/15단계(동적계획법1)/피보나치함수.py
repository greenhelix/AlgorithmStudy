# https://www.acmicpc.net/problem/1003
# 다이나믹 프로그래밍

case = int(input())

zero = [1, 0, 1]  # 0 호출 수 0 , 1, 2 까지 나타냄
one = [0, 1, 1]  # 1 호출 수 0 , 1, 2 까지 나타냄


def pibona(num):
    length = len(zero)
    if length <= num:
        for i in range(length, num + 1):
            print('hey', i)
            # 3부터는 0 호출수를 적어주기 위해 append를 해준다.
            zero.append(zero[i - 1] + zero[i - 2])
            one.append(one[i - 1] + one[i - 2])
    # 마지막 수가 아니라 해당 num 의 값을 찾아서 추출한다.
    print(zero[num], one[num])


for _ in range(case):
    pibona(int(input()))
