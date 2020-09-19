# flood fill , 2차원 배열 내부 것들을 어떻게 처리할 것인가
# 함수 단위로 출력을 하게 되면 테스트를 했을때 어느 부분에서 에러가 나는지 잘 확인이 가능하다
def new_array(N):
    return [[False for i in range(10)] for _ in range(N)]


N, K = map(int, input().split())
M = [list(input()) for _ in range(N)]
ck = new_array(N)
ck2 = new_array(N)


# 방향벡터 설정 상하좌우
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]


def dfs(x, y):
    ck[x][y] = True
    ret = 1
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck[xx][yy] or M[x][y] != M[xx][yy]:
            continue
        ret += dfs(xx, yy)
    return ret


def dfs2(x, y, val):  # 지우기
    ck2[x][y] = True
    M[x][y] = '0'
    for i in range(4):
        xx, yy = x + dx[i], y + dy[i]
        if xx < 0 or xx >= N or yy < 0 or yy >= 10:
            continue
        if ck2[xx][yy] or M[xx][yy] != val:
            continue
        dfs2(xx, yy, val)


def down():  # 내려오는 함수
    for i in range(10):
        tmp = []
        for j in range(N):
            if M[j][i] != '0':
                tmp.append(M[j][i])
        for j in range(N - len(tmp)):
            M[j][i] = '0'
        for j in range(N - len(tmp), N):
            M[j][i] = tmp[j-(N-len(tmp))]


while True:
    exist = False
    ck = new_array(N)
    ck2 = new_array(N)
    for i in range(N):
        for j in range(10):
            if M[i][j] == '0' and not ck[i][j]:
                continue
            res = dfs(i, j)  # 갯수 세기
            if res >= K:
                dfs2(i, j, M[i][j])  # 지우기
                exist = True

    if not exist:
        break
    # 내려오는 함수
    down()

for i in M:
    print(''.join(i))
