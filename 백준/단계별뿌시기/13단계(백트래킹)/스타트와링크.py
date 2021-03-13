# https://www.acmicpc.net/problem/14889
from itertools import combinations as cb
import sys
input = sys.stdin.readline
n = int(input())
stat = [list(map(int, input().split())) for _ in range(n)]
num = [i for i in range(n)]
res = float('inf')


def balance():
    global res

    for config in cb(num, n // 2):
        start_team = list(config)
        link_team = list(set(num) - set(config))
        print('start:', start_team, 'link:', link_team)
        start_stat, link_stat = 0, 0
        start_comb = cb(start_team, 2)
        link_comb = cb(link_team, 2)
        for i, j in start_comb:
            start_stat += stat[i][j] + stat[j][i]

        for i, j in link_comb:
            link_stat += stat[i][j] + stat[j][i]

        print('now Stat------------------')
        print('start:', start_stat, 'link:', link_stat,
              'gap:', abs(start_stat - link_stat))
        if res > abs(start_stat - link_stat):
            res = abs(start_stat - link_stat)


balance()
print('RESULT>>>>>>>>>>>>>>')
print(res)
