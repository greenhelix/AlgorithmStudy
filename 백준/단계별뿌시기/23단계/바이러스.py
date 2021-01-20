# https://www.acmicpc.net/problem/2606
# DFS / BFS
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7

pc = int(input())
l = int(input())

# map을 만든다.  비어잇는 공간을 노드갯수+1 만큼 형성한다. 둘레에 0을 한번 감싸줌
matrix = [[0] * (pc+1) for _ in range(pc+1)]
print(*matrix, sep='\n')

for _ in range(l):
    link = list(map(int, input().split()))  # 연결관계를 리스트르 받아낸다.
    # map상에 있는 이차원 배열에 해당 위치로 관계가 있을시 1
    # 관계가 없으면 0으로 채워준다.
    # map[시작점][도착점]
    matrix[link[0]][link[1]] = 1
    # 1 3 , 3 1 둘다 적용해주기위해 위치를 바꿔서 입력
    matrix[link[1]][link[0]] = 1

print(*matrix, sep='\n')  # list 한줄씩 출력하는 방법


def findZombie(start, m):
    for i in range(len(m[start])):
        if m[start][i] and i not in track:
            print('감염 발견=', i)
            track.append(i)
            print('감염된 pc들=', track)
            findZombie(i, m)


track = []
findZombie(1, matrix)

print(len(track) - 1)
