# https://www.acmicpc.net/problem/10757
# 간단하게 파이썬은 크기가 큰 수도 계산이 된다.
# 그러나 자반, C++만해도 이러한 큰 수는 계산이 불가능하다.
# 0<= A,B < 10^10000 이라 할때 A+B를 출력하는 방법을
# 다른 언어의 방식을 파이썬으로 구현하겠다.

# 핵심은 문자열로 각 자리 수를 계산한다.

a, b = map(str, input().split())
aSize, bSize = len(a), len(b)
result = ''
up = 0
while aSize > 0 or bSize > 0:
    # java 에서 ? 문을 파이썬에서는 if else 로 바로 표현 가능하다.
    if aSize < 0:
        c1 = 0
    else:
        c1 = int(a[aSize-1])
    # 위의 표현을 c2로 조건문 표현이 간단하게 된다.
    c2 = 0 if bSize < 0 else int(b[bSize-1])
    # print(c1, c2)
    plus = c1 + c2 + up

    c0 = plus % 10
    up = plus // 10
    # print('c0=', c0, 'up=', up)
    result = str(c0) + result
    aSize -= 1
    bSize -= 1
    # print('size=', aSize)
if up > 0:
    result = str(up) + result

print(result)

# 이러한 문제는 파이썬에서는 이렇게 풀 필요없이 아래와 같이 풀수도 있다.
a, b = map(int, input().split())
print(a+b)
