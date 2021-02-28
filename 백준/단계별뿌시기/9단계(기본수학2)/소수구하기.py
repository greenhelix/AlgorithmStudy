# # https://www.acmicpc.net/problem/1929
# # 아리토스테네스 체 구하기
a, b = map(int, input().split())


def aristo(a, b):
    b += 1
    show = [True] * b  # t/f틀을 구성
    # 범위끝의 제곱근추출
    for i in range(2, int(b ** 0.5)+1):  # 제곱근 까지만 추출
        if show[i]:  # True라면 검사.
            for j in range(2*i, b, i):  # 1의 배수들을 False로 변환한다.
                show[j] = False
    # 1초과, True이면, 소수로 추출
    for i in range(a, b):
        if i > 1 and show[i] == True:
            print(i)


aristo(a, b)
