# https://www.acmicpc.net/problem/1780

# 만약 종이가 모두 같은 수로 되어 있다면 이 종이를 그대로 사용한다.
# (1)이 아닌 경우에는 종이를 같은 크기의 9개의 종이로 자르고, 각각의 잘린 종이에 대해서 (1)의 과정을 반복한다.

# 9분할 하는 분할 정복이다.

# 9
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 0 0 0 1 1 1 -1 -1 -1
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 1 1 1 0 0 0 0 0 0
# 0 1 -1 0 1 -1 0 1 -1
# 0 -1 1 0 1 -1 0 1 -1
# 0 1 -1 1 0 -1 0 1 -1

# 10   -1 인 경우
# 12   0 인 경우
# 11   1 인 경우


def quad_tree(x, y, n):
    global matrix, minus, zero, one
    check = matrix[y][x]
    flag = False

    for i in range(x, x + n):
        if flag:
            break

        for j in range(y, y + n):
            if matrix[j][i] != check:

                # 9분면으로 자르기! 9개의 재귀가 필요하다.(핵심)

                quad_tree(x, y, (n//3))
                quad_tree(x + (n//3), y, (n//3))
                quad_tree(x, y + (n//3), (n//3))
                quad_tree(x + (n // 3), y + (n // 3), (n // 3))

                quad_tree(x + 2*(n//3), y, (n//3))
                quad_tree(x + 2 * (n // 3), y + (n // 3), (n // 3))

                quad_tree(x + (n//3), y + 2*(n//3), (n//3))
                quad_tree(x, y + 2 * (n // 3), (n // 3))

                quad_tree(x + 2 * (n // 3), y + 2 * (n // 3), (n // 3))

                flag = True
                break

    if not flag:
        if matrix[y][x] == -1:
            minus += 1
        elif matrix[y][x] == 0:
            zero += 1
        else:
            one += 1


n = int(input())
matrix = []
for _ in range(n):
    matrix.append(list(map(int, input().split())))

minus, zero, one = 0, 0, 0

quad_tree(0, 0, n)
print(f'{minus}\n{zero}\n{one}')
