# https://www.acmicpc.net/problem/2839
# 수학 / 다이나믹 프로그래밍 / 그리디 알고리즘
# 설탕n킬로그램배달 - 3킬로그램 / 5킬로그램봉지로포장
# 최대한적은봉지로배달
# 3<=n <= 5000
# 최소봉지 갯수 , 정확하지 않다면 -1 출력


# 큰단위로 나누고, 다음 단위는 -를 통해서 n의 값을 변화준다.
# 이렇게 하면 반복되는 값의 n을 큰 단위의 기준으로 먼저 나누고 나머지를
# 작은 값으로 뺴게 되어 딱 떨어지는 값을 구할 수 있다.

n = int(input())
count = 0
while n != 0:
    if n % 5 == 0:
        count += n // 5
        break
    elif n % 5 != 0:
        n = n - 3
        count += 1
    if n < 0:
        count = -1
        break
print(count)
