# https://www.acmicpc.net/problem/2667
# 그래프이론 / 그래프탐색 / BFS / DFS
# 지도가 있고 1은 집이 있는 곳 , 0 은 없는 곳이다. 연결된 집의 모임인 단지를 정의 , 단지에 번호를 부여한다.
# 연결의 의미는 좌우 or 위아래 다른집이 있는 경우이다. 대각선은 연결 아님.
# 지도를 보고, 단지수를 출력하고 각 단지에 속하는 집의 수를 오름차순으로 정렬 출력.

n = int(input())
houseMap = []
for _ in range(n):
    houseMap.append(list(map(int, input())))

print(*houseMap, sep='\n')

# 방향 벡터
rl = [-1, 1, 0, 0]  # 위아래
ud = [0, 0, 1, -1]  # 좌우

complex = []  # 단지 그룹 선언


def bfs(x, y):
    queue = [[x, y]]  # 해당 좌표를 큐에 리스트 형태로 담는다.
    houseMap[x][y] = 0  # 해당 좌표대로 시작점을 찍는다.
    count = 1  # 너비탐색을 들어왔다면 집이 한개있는것이기 때문에 일단 카운트 하여 1로 시작한다.
    while queue:
        a, b = queue[0][0], queue[0][1]  # 해당 좌표의 값을 a, b에 저장시킨다.
        del queue[0]  # 사용할 것이니 끄내고 나머지는 삭제 한다.
        for i in range(4):  # 4가지 방향인만큼 값들을 돌려줘본다.
            xx = a + rl[i]  # 위아래 탐색한다
            yy = b + ud[i]  # 좌우 탐색한다.
            # 가장자리 안의 인덱스와 해당 좌표값들이 지도에 1인지 확인
            if 0 <= xx < n and 0 <= yy < n and houseMap[xx][yy] == 1:
                houseMap[xx][yy] = 0  # 집을 카운팅하였으니 0으로 만들어주고 갱신한다.
                queue.append([xx, yy])
                count += 1  # 집의 수를 증가시킨다.
    complex.append(count)  # 반복문을 나온 해당 집의 수를 단지수별로 저장한다.


for i in range(n):
    for j in range(n):
        if houseMap[i][j] == 1:  # 집이 있는 경우 너비탐색 시작시킨다.
            bfs(i, j)

complex.sort()  # 오름차순으로 정렬한다.
print(complex)
print(len(complex))
for i in complex:
    print(i)
