# https://www.acmicpc.net/problem/9184
'''Dynamic Programming / Memoization
메모이제이션은 재귀함수를 진행할때, 값을 저장하여 반복되는 계산을 진행하지 않는 방법이다.
재귀의 단점을 보완하는 중요한 개념이다. 동적계획법의 핵심이 되는 기술이다.'''

MAX = 21    # 0 ~ 20 이 범위이기 때문에 21로 범위를 잡아준다.
# 입력값이 abc 세개 이기 때문에 범위를 3차 배열로 형성
dp = [[[0] * MAX for _ in range(MAX)] for __ in range(MAX)]
# dp테이블에는 각 계산값이 담기는 형태로 들어간다.


def w(a, b, c):

    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    # 값이 이미 존재한다면 그 값을 바로 리턴한다.(메모이제이션)
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
