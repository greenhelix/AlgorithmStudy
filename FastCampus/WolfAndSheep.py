# 방향벡터에 관련된 문제이다. 백준 16956번 문제이다. 늑대와 양

# 문제이서 입력되는 목장의 범위를 R, C에 나눠서 담아준다.
R, C = map(int, input().split())
# 다음의 각 양과 늑대의 위치를 나타내는 값을 입력값마다 범위 세로의 값기준으로 반복받아준다.
M = [list(input()) for i in range(R)]

dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]  # 시계방향 방향벡터를 설정해준다.

ck = False

for i in range(R):
    for j in range(C):
        if M[i][j] == 'W':  # 늑대를 발견한 경우
            # 반복문을 통해 울타리의 위치를 해당 늑대위치를 기준으로 시계방향으로 돌린다.
            for w in range(4):
                # 시계방향으로 돌린 새로운 위치값 ii, jj를 예외상황을 추려준다
                ii, jj = i + dx[w], j + dy[w]
                if ii < 0 or ii == R or jj < 0 or jj == C:
                    continue
                # 주변에 양이 존재한다면 CK를 통해 체크를 해준다.
                if M[ii][jj] == 'S':
                    ck = True
# 늑대 주변에 바로 양이 존재한다면 해당 양의 위치에는 울타리설치불가
if ck:
    print(0)
# 그렇지 않다면 울타리 설치가 가능하기때문에
else:
    print(1)  # 1을 출력해준뒤
    # 반복문을 통해서 해당 위치에 SW가 없는지 확인하고 해당 위치에 D를 삽입해준다.
    for i in range(R):
        for j in range(C):
            if M[i][j] not in 'SW':
                M[i][j] = 'D'
# 이렇게 완성된 값들을 배열을 join을 통해 합쳐서 출력해준다.
for i in M:
    print(''.join(i))
