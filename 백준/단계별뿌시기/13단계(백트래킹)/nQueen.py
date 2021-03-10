# https://www.acmicpc.net/problem/9663
# 대표적인 백트래킹 문제 이다. / 브루트 포스 알고리즘(다 찾는거)
n = int(input())  # n은 퀸의 갯수를 뜻한다. 그리고 n*n의 체스판을 가진다.
row = [0 for i in range(16)]  # 매트릭스를 구성한다.
result = 0


def isTrue(x):
    for i in range(1, x):
        # 같은 위치인지, 대각선으로 같은지 확인하는 조건문
        if row[x] == row[i] or abs(row[x] - row[i]) == x - i:
            return False
    return True


def dfs(cnt):  # 1번 여왕부터 n번여왕까지의 깊이 탐색을 시작
    global result
    if cnt > n:  # 시작값은 1이다.
        result += 1  # 최종적으로 이 조건문에 들면, result가 쌓인다.
        # 전체 반복이 완료되면 자동 종료된다.
    else:
        for i in range(1, n + 1):
            row[cnt] = i  # 매트릭스에 해당 cnt 의 값 1부터 값이 들어간다.
            if isTrue(cnt):  # 대각, 십자각 사이에 있는지 확인하고 True이면 해당사항없으므로
                dfs(cnt + 1)  # cnt를 +1하여 다시 탐색을 돌려준다.


dfs(1)
# 종료된 result값이 남게 되고, 그것을 출력만하면된다.
print(result)  # n개의 퀸이 서로 공격할 수 없는 경우의 수를 출력한다.
