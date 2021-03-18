# https://www.acmicpc.net/problem/1463
'''
1로 만들기, 정수 x에 사용할 수 있는 연산 - 세가지 - 3으로 나눠지면, 3으로 나누고
2로 나눠지면, 2로 나눈다. 1을 뺀다
N이 주어졌을때, 위의 연산을 활용하여 결과를 1로 만들려 한다. 
연산 사용 횟수 최소값은?

1<=N<=1000000
'''
n = int(input())+1

dp = [-1 for _ in range(n)]
print('dp:', dp)

for i in range(1, n):
    print(i, '!!')
    dp[i] = dp[i - 1] + 1  # dp[1] = 0
    print(dp)
    if i % 2 == 0:
        dp[i] = min([dp[i], dp[i // 2] + 1])
        print(i, '//2!', dp)
    if i % 3 == 0:
        dp[i] = min([dp[i], dp[i // 3] + 1])
        print(i, '//3!', dp)

print('dp now:', dp)
print(dp[-1])
