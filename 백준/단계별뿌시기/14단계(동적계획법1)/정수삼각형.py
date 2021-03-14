# https://www.acmicpc.net/problem/1932
'''
핵심은 메모이제이션의 개념을 활용하려 했느냐이다. 
이 문제의 경우 마지막까지 모든 경우의 수를 다 계산해서 최대값을 추출해야 한다. 
그러나, 이렇게 되는 경우 너무 많은 경우가 발생하여 느려진다. 
그래서 각 층으로 내려갈 수록 합의 기록을 축적해둔뒤, 최종 마지막에 최대값을 추출해야한다. 

양 끝 맨 왼, 오른쪾의 경우는 그냥 이전합의 수에서 해당 수를 더해주면 그만이다. 
그러나 가운데 수들은 양쪽의 수들에 의해 다양한 값들의 경우가 발생한다. 
이러한 경우 max() 이용해서 해당 값들의 발생중 가장 큰 값을 추출해 내면된다. 
그렇게 된우, 이러한 값들을 matrix에 최신화 시켜서 다음 층에서는 이러한 계산이 반복안하게 만든다.
- 경로를 찾기는 어려운 풀이이다. - 하지만 이런 개념이면 경로 추적도 가능하다. 

'''
# 5
# 7
# 3 8
# 8 1 0
# 2 7 4 4
# 4 5 2 6 5
import sys
input = sys.stdin.readline
n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

case = 2  # 초기 경우의수는 2가지이다.

for i in range(1, n):  # 2층부터 시작한다.
    for j in range(case):
        # 맨 왼쪽의 경우 한 가지만 경우가 나온다.
        if j == 0:
            matrix[i][j] += matrix[i - 1][j]
        # 맨 오른쪽의 경우도 한가지만 나온다.
        elif j == i:
            matrix[i][j] += matrix[i - 1][j - 1]
        # 중간에는 여러 경우의 수가 발생하는데, 그중에서 max()만 찾아서 입력해준다.
        else:
            matrix[i][j] += max(matrix[i - 1][j - 1], matrix[i - 1][j])
    case += 1

# 최종적으로 최대 값들만 각 층별로 경우의 수의 값들이 저장된다.
print(matrix)
print(max(matrix[n - 1]))
