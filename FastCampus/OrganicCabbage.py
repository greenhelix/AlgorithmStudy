import sys
sys.setrecursionlimit(10000)

T = int(input())
# 전역 변수로 선언해줘서 다 공유되게 해준다.
B, ck = [], []

# 방향벡터이다. 무조건 알아야한다. 이 방향들은 위 아래 좌 우 를 상징하는 것이다.
dx, dy = [1, 0, -1, 0], [0, 1, 0, -1]


def dfs(x, y):  # 4방향으로 탐색을 하는 함수를 선언해주는 것이다.
    global B, ck
    if ck[x][y] == 1:
        return
    ck[x][y] = 1

    for i in range(4):
        # xx와 yy는 다음 순회의 위치라고 보고, 기존 x,y에 dx, dy의 값들이 순서대로 적용되면서 4방향으로 순회를 돈다.
        xx, yy = x + dx[i], y + dy[i]
        # 이렇게 적용된 xx, yy값들이 B 와 ck의 위치로 들어가서 해당 값들이 0 또는 1인지 확인하여 분석하고
        if B[xx][yy] == 0 or ck[xx][yy] == 1:
            continue
        # 그것이 아니라면 다시 dfs로 재귀용법을 통해 다시 순회하면된다.
        dfs(xx, yy)


def process():
    global B, ck
    # 주어진 연속 세 개의 수는 각 가로 / 세로 / 벌레의 수를 나타내기 때문에 split을 통해 나눈후 int로 map해준다.
    M, N, K = map(int, input().split())
    # 주어진 배열의 크기를 양쪽 한칸 씩 늘려서 만든다.
    B = [[0 for i in range(50 + 2)] for _ in range(50 + 2)]
    # 탐색한 부분을 확인 할 수 있는 체크배열을 하나 더 생성해준다.
    ck = [[0 for i in range(50 + 2)] for _ in range(50 + 2)]
    # 세로와 가로로 주기때문에 잘 확인하고 적는다.
    for _ in range(K):
        # 벌레의 수만큼 각 벌레의 위치값이 0 0 이런식으로 들어오기 때문에 split을 통해 분할하여 X, Y로 넣어준다.
        X, Y = map(int, input().split())
        # 여기서 X, Y값이 서로 어디의 위치인지 잘 파악하고 넣어줘야 한다. 예를들어 1 0 이라고 하면 x는 세로이고 0은 y값이 므로, 위치를 바꿔서 넣어줘야한다.
        B[Y + 1][X + 1] = 1

    # 최소값을 나타내 주는 ans를 선언해준다.
    ans = 0

    # 이제 각 범위 별로 반복문을 형성해주고
    for i in range(1, N + 1):
        for j in range(1, M + 1):
            # 각 위치별로 확인해준다. 배추밭에서 그 지점이 0이거나 체크한 부분이 1이라면(체큰한 것이므로) 계속진행되게 한다.
            if B[i][j] == 0 or ck[i][j] == 1:
                continue
            # 그 외의 경우는 주변을 탐색하지 않았다는 것이기 때문에 dfs함수를 이곳에 적용해준다.
            dfs(i, j)

            ans += 1
    print(ans)  # 그리고 해당 ans를 프린트해줘야 답이 출력된다.


# T의 값만큼 반복해서 진행한다.
for _ in range(T):
    process()
