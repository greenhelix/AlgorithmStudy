# dfs와 bfs 를 딕셔너리를 통해서 구현하기
from sys import stdin
read = stdin.readline                # readline을 통해서 값을 받는다
matrix = {}
for i in range(int(read())):         # pc의 갯수만큼 matrix를 구성하는데, 1칸 더 늘려서 받는다.
    matrix[i + 1] = set()
for j in range(int(read())):         # pc관계쌍의 갯수를 받아서 그 수만큼 반복문을 수행
    a, b = map(int, read().split())  # 관계를 a,b로 나눠서 담는다.
    matrix[a].add(b)                 # a,b를 교환법칙을 통해서 다 담아준다.
    matrix[b].add(a)

for s, e in matrix.items():        # dictionary 출력이쁘기하는 방법
    print("{} : {}".format(s, e))  # https://rfriend.tistory.com/560


def dfs(start, matrix):      # 깊이우선탐색을 구현한다. 시작점이 필요하다면 파라미터를 추가
    for i in matrix[start]:  # 시작점부터 탐색을 시작한다.
        if i not in track:  # track이라는 경로에 중복이 없는지 확인하면서 찾는다.
            print('감염 발견=', i)
            track.append(i)  # 경로를 추가해준다.
            print('감염된 pc들=', track)
            dfs(i, matrix)   # 찾은 경로를 다시 시작점으로두고 찾는다.


track = []  # 경로를 담아줄 리스트를 선언해준다.
dfs(1, matrix)
print(track)
print(len(track) - 1)
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
