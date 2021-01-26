# https://www.acmicpc.net/problem/9184
'''if a <= 0 or b <= 0 or c <= 0, then w(a, b, c) returns:
    1

if a > 20 or b > 20 or c > 20, then w(a, b, c) returns:
    w(20, 20, 20)

if a < b and b < c, then w(a, b, c) returns:
    w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)

otherwise it returns:
    w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)'''
# 위의함수를구현하는것은매우쉽다.하지만,
# 그대로구현하면값을구하는데매우오랜시간이걸린다.
# (예를 들면, a=15, b=15, c=15)
# a, b, c가 주어졌을 때, w(a, b, c)를 출력하는 프로그램을 작성하시오.
# 입력은 세 정수 a, b, c로 이루어져 있으며, 한 줄에 하나씩 주어진다.
# 입력의 마지막은 -1 -1 -1로 나타내며, 세 정수가 모두 -1인 경우는 입력의 마지막을 제외하면 없다.

# 입력으로 주어진 각각의 a, b, c에 대해서, w(a, b, c)를 출력한다.

MAX = 21    # 0 ~ 20 이 범위이기 때문에 21로 범위를 잡아준다.
# 입력값이 abc 세개 이기 때문에 범위를 3차 배열로 형성
dp = [[[0] * MAX for _ in range(MAX)] for __ in range(MAX)]
# dp테이블에는 각 계산값이 담기는 형태로 들어간다.


def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 값이 이미 존재한다면 그 값을 바로 리턴한다.
    if dp[a][b][c]:
        print(f'dp[{a}][{b}][{c}] = {dp[a][b][c]}')
        return dp[a][b][c]

    if a < b < c:
        print(f'a<b<c 의 경우이다. dp[{a}][{b}][{c}]')
        dp[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    print(f'그밖의 경우 의 경우이다. dp[{a}][{b}][{c}]')
    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + \
        w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]


while True:

    a, b, c = map(int, input().split())

    # 재귀함수를 멈추는 조건
    if (a, b, c) == (-1, -1, -1):
        break

    # 출력방식은 변경 가능하다.
    print("w(%d, %d, %d) = %d" % (a, b, c, w(a, b, c)))
