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


def bfs(start, matrix):
    queue = [start]                    # 시작점을 입력해서 실행해준다.
    while queue:                       # 새로입력된 Queue가 있다면 거기서 다음 것을 꺼내서 실행
        for i in matrix[queue.pop()]:  # {2,5}를 순서대로 검색
            if i not in track:
                print('감염 발견=', i)
                track.append(i)        # 경로는 축적해준다.
                print('감염된 pc들=', track)
                queue.append(i)        # Queue에 넣어준뒤 다음 탐색 대상을 올려둔다.


track = []
bfs(1, matrix)
print(track)
print(len(track)-1)
# 7
# 6
# 1 2
# 2 3
# 1 5
# 5 2
# 5 6
# 4 7
