import sys
sys.setrecursionlimit(10000)

T = int(input())
B, ck = [], []

dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def process():
    global B, ck
    M, N, K = map(int, input().split())
