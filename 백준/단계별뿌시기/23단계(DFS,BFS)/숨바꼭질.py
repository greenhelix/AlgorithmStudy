# https://www.acmicpc.net/problem/1697
import sys
from collections import deque
n, k = map(int, sys.stdin.readline().split())
print(n, '에서', k, '으로 가야한다.')
matrix = [0] * 100001    # 반드시 평면, 직선사잉여도 매트릭스를 구성해야 한다.
queue = deque()


def bfs(x, y, time_check):
    queue.append(x)
    while queue:
        print('IN while')
        a = queue.popleft()
        print('this a : ', a, ': queue:', queue)
        if a == y:
            return time_check[a]

        for i in (a + 1, a - 1, 2 * a):
            print('this i : ', i)
            # 조건문은 해당 값의 최대값을 명시해야하며, 범위를 나타내주고, 시간 테이블에서
            # 비어있던 값인 지 확인해야 한다.
            if 0 <= i < 100001 and time_check[i] == 0:
                # 해당 값의 현재 걸린 시간을 업데이트 해준다.
                time_check[i] = time_check[a] + 1
                # 큐에 해당 값을 추가해 둔다.
                queue.append(i)


print(f'{bfs(n, k, matrix)}초가 걸립니다.')
