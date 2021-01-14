# https://www.acmicpc.net/problem/2292
# 수학
# 육각형벌집
# 중앙1 - -> 이웃 + 1증가
# 숫자N, 중앙1에서N번까지몇개의최소갯수방지나가나
# 시작끝포함.
# 13까지는3개58까지는5개지나감.
# 입력: 1부터1억
# 출력: 최소 지나간 방 갯수

N = int(input())
max = 1
size = 6
step = 1
while N > max:
    step += 1
    max += size
    size += 6
print(step)
