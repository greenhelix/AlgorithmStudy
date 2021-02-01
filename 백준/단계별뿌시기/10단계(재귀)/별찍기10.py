# https://www.acmicpc.net/problem/2447
# 분할 정복 / 재귀
n = int(input())

pattern = [[' ']*n for _ in range(n)]  # 빈공간을 먼저 형성해준다. 2차원 배열로 형성


def star(size, x, y):
    if size == 1:   # 1의 경우 최종 상태이기 때문에 별을 붙여준다.
        # 즉, 이 특정 경우 외에는 재귀가 멈추지 않고, 해당 x, y과 값이 안뜬다면, 그곳은  ' ' 의 형태로 유지
        pattern[y][x] = '*'
    else:
        nextSize = size // 3  # 3이상의 경우 사용되어 계산된다.
        for yy in range(3):
            for xx in range(3):
                if xx != 1 or yy != 1:  # 중간값을 제외한 나머지 값들은 다시한번 Star()을 돌려주어 가운데가 비게 별을 붙여준다.
                    star(nextSize, x + xx * nextSize, y + yy * nextSize)


star(n, 0, 0)
print(*pattern, sep='\n')
for k in pattern:
    print(''.join(k))
