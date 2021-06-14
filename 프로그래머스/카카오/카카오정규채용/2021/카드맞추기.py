import math
import queue


# 굳이 Board에 변형된 상태를 반영해서 진행할 필요가 없었다.
# 단순히 카드의 쌍을 삭제했다는 표시와 최단거리 및 키의 조작횟수를 카운트 하면된다.
# 비트연산을 통해 각 비트 번호별로 카드번호로 측정하여 진행하면 된다.


# 전역변수
Board = []
Allcard = {}
Allremoved = 1
MinCnt = math.inf  # 최소 조작횟수를 담아줄 전역변수
D = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 상하좌우 방향

# 제거된 카드 상태 removed, srt시작과 dst목적지 파라미터 준다.


def bfs(removed, src, dst):
    visited = [[False for _ in range(4)] for _ in range(4)]
    q = queue.Queue()

    q.put(src)

    while q:
        curr = q.get()  # curr은 현재 위치

        if curr[0] == dst[0] and curr[1] == dst[1]:  # 현재 위치가 목적지와 같다면, 종료
            return curr[2]  # 세번째 옵션인 조작횟수를 반환한다.

        '''
        상하좌우버튼을 먼저 누를 상태에서 ctrl를 추가해준다면, 

        '''
        for i, j in D:  # 방향 상하좌우 반영해준다.
            nr = curr[0] + i
            nc = curr[1] + j

            if nr < 0 or nr > 3 or nc < 0 or nc > 3:  # 범위 밖은 생략

                continue  # skip해주는게 더 좋은듯

            if not visited[nr][nc]:  # 방문한적이 없다면,

                visited[nr][nc] = True  # 방문했다고 마킹한다.

                q.put((nr, nc, curr[2] + 1))  # 상하좌우, 방향키 입력 한 상태

            # CTRL키를 누르고 이동했다면, 더 이동이 되는것이다.
            # 얼마나 더 이동 할 수 있나 본다. crtl 키 눌렀을 때, 최대 2번 이동이 가능하다
            # 즉, ->를 누르면 한칸이동인데, ctrl ->을 누르면 두칸 더 이동이 가능하다.
            # 이 범위는 맵이 넓으면 커진다.
            for ctrl in range(2):  # 그래서 범위를 2로 해준다.

                if removed & 1 << Board[nr][nc] == 0:  # 카드를 만나거나 경계면에 만났을때
                    break

                # 맵 밖으로 나가는 경우.
                if nr + i < 0 or nr + i > 3 or nc + j < 0 or nc + j > 3:
                    break

                nr += i  # 그 외의 경우는 더 이동 시킨다.
                nc += j

            # ctrl이동이 됐을때만 이쪽으로 온다. 그런 경우 현재위치를 반영해주는 조건문을 해준다.
            # 방문 기록도 추가해준다.
            if not visited[nr][nc]:

                visited[nr][nc] = True

                q.put((nr, nc, curr[2] + 1))  # ctrl 상하좌우, 방향키 입력 한 상태

    return math.inf  # 혹시 이상있는 경우, 무한대값을 리턴하게 한다. 최소값을 만드는 것이므로 이렇게 해준다.


def permutate(cnt, removed, src):  # 재귀적으로 permutate를 진행시킨다.
    global MinCnt

    # cnt보다 작다면 더이상 탐색을 진행하지 않는다.
    # 가지치기 하는 것이다. # Backtracking부분이다.
    if cnt >= MinCnt:
        print(MinCnt, '이 더 작거나 같으니 안찾는다.', cnt)
        return

    if removed == Allremoved:  # 종료 조건
        print('>>>종료:', MinCnt, cnt)
        MinCnt = min(MinCnt, cnt)
        return

    for num, card in Allcard.items():  # 탐색, 카드번호는 num, 각 카드의 좌표는 card
        # 여기서 1은 0번 카드 , 즉 빈공간을 의미한다.
        # 이 카드가 이미 삭제된 것이라면, 스킵한다. AND논리연산으로, 카드가 같은 경우, 제거했다는 것이다.
        if removed & 1 << num:
            print('num:', num, '카드는 제거했다.\n')
            continue

        print('카드번호:', num, '은 아직 제거 안했다.')
        # 순차와 역순의 조작횟수cnt를 가져온다.
        # 카드가 두장이기 때문에, src현재포인터에서 card[0]또는 card[1]을 쓴다.
        # card[0] -> card[1] , card[1] -> card[0]
        # enter 2 추가해준다.
        순차 = bfs(removed, src, card[0]) + bfs(removed, card[0], card[1]) + 2
        역순 = bfs(removed, src, card[1]) + bfs(removed, card[1], card[0]) + 2
        print(f'현재위치:{src}이고, 카드{Board[src[0]][src[1]]}에서 카드{num}까지의 최단거리는')
        print(
            f'{num}카드를 찾기위해 {card[0]}부터 찾는다면\n현재조작횟수:{cnt}에서 모든 조작횟수는 {cnt+순차}이다.')
        print(
            f'{num}카드를 찾기위해 {card[1]}부터 찾는다면\n현재조작횟수:{cnt}에서 모든 조작횟수는 {cnt+역순}이다.')
        # 순차와 역순의 횟수를 가져와서, 다시 재귀로 cnt에 추가하여 계산해준다.
        # permutate(조작횟수, 제거상태, 포인터)
        permutate(cnt + 순차, removed | 1 << num, card[1])
        permutate(cnt + 역순, removed | 1 << num, card[0])


def solution(board, r, c):
    global Board, Allcard, Allremoved
    Board = board
    print(*board, sep='\n')

    for i in range(4):
        for j in range(4):

            num = Board[i][j]

            if num:
                ''' Allcard는 모든 카드가 제거 되었는지 확인하는 변수이다. 
                1에 <<num 만큼 시프트 연산을 해준뒤, Allremoved에 반영해준다.
                카드가 발견될 때마다, Allremoved조건을 만족하게 하기 위해 반영해준다.
                나중에 이것은 모든 카드가 제거 되었는지 확인하는 지표가 된다.'''
                Allremoved |= 1 << num

                '''카드가 있는 곳의 좌표를 저장해주고, 옵션 0을 붙여준다.
                Dict에서 같은 키 값인 경우 카드를 넣어주는 방법이다.
                따로 범위를 설정하지 않고 이렇게 조건문으로 나눠서 담을 수 있다.'''
                if num in Allcard:  # 카드가 한장이라도 있다면, 추가해준다.
                    Allcard[num].append((i, j, 0))
                else:  # 카드가 등록되지 않았다면, 등록해준다.
                    Allcard[num] = [(i, j, 0)]

    print('Allcard:')
    print(*Allcard.items(), sep='\n')

    # 조합을 만들어, 순차와 역순의 조합을 실행해준다. permutate(cnt, removed, src) 으로 구성되었는데,
    # Allremoved도 1부터 반영했으므로, permu에서도 1로 시작하여 계속 재귀적으로 반영되게 한다.
    # cnt는 조작횟수이다.  0번 카드 즉, 빈공간만 다 제거했다는 가정하에 removed를 1로 입력해준다.
    permutate(0, 1, (r, c, 0))  # src 는 커서 위치인데, 0의 추가 옵션을 준다.

    return MinCnt


board1 = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]

r1, c1 = 1, 0
print('move:', solution(board1, r1, c1))
