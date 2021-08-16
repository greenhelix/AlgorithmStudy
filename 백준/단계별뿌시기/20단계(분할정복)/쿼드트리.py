# https://www.acmicpc.net/problem/1992

# 흑백 영상을 압축하여 표현하는 데이터 구조로 쿼드 트리(Quad Tree)라는 방법이 있다.
# https://www.acmicpc.net/JudgeOnline/upload/201007/qq.png

# 4등분하는 것이 기본 개념이다.


import sys
input = sys.stdin.readline


def quad_tree(n, y, x):

    if n == 1:
        print(image[y][x], end="")
        return

    flag = True

    for i in range(y, y + n):
        if not flag:
            break
        for j in range(x, x + n):
            if image[i][j] != image[y][x]:
                flag = False
                break

    if flag:
        print(image[y][x], end="")

    else:
        quad = n // 2
        print("(", end="")
        quad_tree(quad, y, x)
        quad_tree(quad, y, x+quad)
        quad_tree(quad, y+quad, x)
        quad_tree(quad, y + quad, x + quad)
        print(")", end="")


n = int(input())
image = [list(input().strip()) for _ in range(n)]
quad_tree(n, 0, 0)
