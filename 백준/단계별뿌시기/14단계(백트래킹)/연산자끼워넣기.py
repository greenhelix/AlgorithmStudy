# https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline
n = int(input())
# 숫자와 연산자를 담는다.
A = list(map(int, input().split()))
operator = list(map(int, input().split()))
max_result, min_result = -1000000001, 1000000001  # 최대,최소를 거꾸로 값을 넣어준다.10억1


def dfs(cnt, result, plus, minus, multiple, divide):
    global max_result, min_result
    if cnt == n:  # 숫자의 갯수가 같아지면 - 연산이 종료되었으므로,
        # result값을 검증해준다. 최대치,최소치에 비해서 선정을 하므로, 값이 갱신된다.
        max_result = max(max_result, result)
        min_result = min(result, min_result)
        return  # 종료 시킨다.

    # 각 연산자의 갯수를 해당 포인터를 줄여주면서 진행한다.
    if plus:        # plus가 있다면 즉, 0이라면 이 조건에 들어가지 않게 된다.
        dfs(cnt + 1, result + A[cnt], plus - 1, minus, multiple, divide)
    if minus:  # minus가 있다면
        dfs(cnt+1, result-A[cnt], plus, minus-1, multiple, divide)
    if multiple:  # multiple이 있다면
        dfs(cnt+1, result*A[cnt], plus, minus, multiple-1, divide)
    if divide:  # divide가 있다면
        dfs(cnt+1, -(-result//A[cnt]) if result < 0 else result //
            A[cnt], plus, minus, multiple, divide-1)  # 음수//양수 의 경우 고려하여 result에 반영


# 초기값을 부여해준다.(값을 생성해주는게 아니라, 주어진 값의 첫 시작점이라고 생각하면된다.)
dfs(1, A[0], operator[0], operator[1], operator[2], operator[3])
print(max_result, min_result, sep='\n')
