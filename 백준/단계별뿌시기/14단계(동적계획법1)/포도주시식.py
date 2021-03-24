# https://www.acmicpc.net/problem/2156
'''
1. 포도주 잔을 선택하면 그 잔에 들어있는 포도주는 모두 마셔야 하고, 마신 후에는 원래 위치에 다시 놓아야 한다.
2. 연속으로 놓여 있는 3잔을 모두 마실 수는 없다. (2잔은 연속 마시기 가능)

포도주는 일렬로 나열되어있다. 
1~n까지의 번호가 붙은 포도주 잔. 
각 포도주 잔에 들어있는 포도주의 양은 주어짐. 

가장 많이 마실수 있도록 하는 프로그램을 만들자. 

1<=n<=10000 
0<포도주 양<=1000 , 정수 

'''
n = int(input())
glass = [int(input()) for x in range(n)]

dp = [0]
# 1번째 잔을 고르는 경우는 그냥 6을 넣어준다.
dp.append(glass[0])

# 2번째 잔을 고르는 경우도 한 경우밖에 없으므로 1,2번째 잔을 더해서 넣어준다. 
if(n > 1):
    dp.append(glass[0] + glass[1])

# 연속 3잔을 마시지 않아야 하므로
# 1 : 이번 포도주를 먹고 이전 포도주를 먹지 않은 경우
# 2 : 이번 포도주를 먹고 이전 포도주도 먹은 경우
# 3 : 이번 포도주를 먹지 않아야 하는 경우
# 위 세가지 경우를 고려하여 max

for i in range(3, n + 1):
    # glass는 0부터 시작하므로 i - 1로 해준다.
    case_1 = glass[i - 1] + dp[i - 2]
    case_2 = glass[i - 1] + glass[i - 2] + dp[i - 3]
    case_3 = dp[i - 1]
    print(i, '번째::', case_1, case_2, case_3)
    # 가장 큰 경우의 수를 산출해준다.
    max_value = max(case_1, case_2, case_3)

    dp.append(max_value)

print(dp[n])
