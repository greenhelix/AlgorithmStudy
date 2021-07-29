# https: // www.acmicpc.net / problem / 10951
# 수학 / 구현 / 사칙연산
while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except EOFError:
        break
# EOFError End of File 입출력이 끝날때까지를 의미.
