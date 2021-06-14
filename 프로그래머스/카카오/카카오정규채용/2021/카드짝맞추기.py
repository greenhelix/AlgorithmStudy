
from collections import deque, defaultdict
from itertools import permutations as perm

global board


def remain_card(board):
    card_set = set()
    card_dict = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j] != 0:
                card_dict[board[i][j]].append([i, j])
                card_set.add(board[i][j])

    return card_set, card_dict


def bfs_find_card(sx, sy, card, board):
    # 카드를 찾고, move에 추가해준뒤, 다시 0체크로 돌아간다.
    short = 0
    fx, fy = 0, 0  # 최단거리 찾은 카드 좌표
    vector = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    shortdict = []
    print('bfs_find_card')
    print('찾을 카드들', card)
    print('카드 찾기')

    # move
    print("MOVE")
    print('card:', card)
    matrix = [[0] * 4 for _ in range(4)]
    q = deque()
    q.append((sx, sy))
    find = 0

    while q:
        x, y = q.popleft()
        print('popleft:', x, y)
        if find == 1:
            break
        for i, j in vector:
            xx = x + i
            yy = y + j

            if 0 <= xx < 4 and 0 <= yy < 4:

                if board[xx][yy] != card:
                    matrix[xx][yy] = matrix[x][y] + 1
                    q.append((xx, yy))

                elif board[xx][yy] == card:
                    matrix[xx][yy] = matrix[x][y] + 1
                    shortdict.append([matrix[xx][yy], xx, yy])
                    find = 1
                    break

    print('최단경로:', shortdict)

    # ctrl move
    print('CTRL MOVE')
    matrix = [[0] * 4 for _ in range(4)]
    q = deque()
    q.append((sx, sy))
    find = 0

    while q:
        x, y = q.popleft()
        print('popleft:', x, y)
        if find == 1:
            break
        for i, j in vector:
            xx = x + i
            yy = y + j
            if 0 <= xx < 4 and 0 <= yy < 4:

                while board[xx][yy] == 0:

                    if xx != 0 and i < 0:
                        xx -= 1
                    elif xx != 0 and i > 0:
                        xx += 1

                    if yy != 0 and j < 0:
                        yy -= 1
                    elif yy != 0 and j > 0:
                        yy += 1

                if board[xx][yy] != card:
                    matrix[xx][yy] = matrix[x][y] + 1
                    q.append((xx, yy))

                elif board[xx][yy] == card:
                    matrix[xx][yy] = matrix[x][y] + 1
                    shortdict.append([matrix[xx][yy], xx, yy])
                    find = 1
                    break

    print('ctrlmove 추가 최단경로:', shortdict)
    short, fx, fy = min(shortdict)
    return short, fx, fy


def bfs_find_pair(sx, sy, pair_cards, board):
    print('bfs_find_pair')
    # 카드의 짝을 찾고, move에 추가해준뒤, 해당 카드종류를 삭제한뒤, 0체크로 돌아간다.
    short = 0
    fx, fy = 0, 0

    card1 = board[sx][sy]
    print()
    print('짝 카드 찾기', pair_cards[card1])

    for i in pair_cards[card1]:
        if [sx, sy] != i:
            fx, fy = i[0], i[1]
    print(sx, sy, '-->', fx, fy)

    vector = [(0, 1), (1, 0), (-1, 0), (0, -1)]

    shortdict = []

    # move
    print("PAIR FIND MOVE")
    matrix = [[0] * 4 for _ in range(4)]
    q = deque()
    q.append((sx, sy))
    find = 0

    while q:
        x, y = q.popleft()
        print('popleft:', x, y)
        if find == 1:
            break
        for i, j in vector:
            xx = x + i
            yy = y + j

            if 0 <= xx < 4 and 0 <= yy < 4:

                if board[xx][yy] != board[sx][sy]:
                    matrix[xx][yy] = matrix[x][y] + 1
                    q.append((xx, yy))

                elif xx == fx and yy == fy:
                    matrix[xx][yy] = matrix[x][y] + 1
                    shortdict.append([matrix[xx][yy], xx, yy])
                    find = 1
                    break

    print('최단경로:', shortdict)

    # ctrl move
    print('PAIR FIND CTRL MOVE')
    matrix = [[0] * 4 for _ in range(4)]
    q = deque()
    q.append((sx, sy))
    find = 0

    while q:
        x, y = q.popleft()
        print('popleft:', x, y)
        if find == 1:
            break
        for i, j in vector:
            xx = x + i
            yy = y + j
            if 0 <= xx < 4 and 0 <= yy < 4:

                while board[xx][yy] == 0:

                    print(xx, yy)

                    if xx != 0 and i < 0:
                        xx -= 1
                    elif xx != 3 and i > 0:
                        xx += 1

                    if yy != 0 and j < 0:
                        yy -= 1
                    elif yy != 3 and j > 0:
                        yy += 1

                    if xx == 0 or xx == 3:
                        break
                    if yy == 0 or yy == 3:
                        break

                if 0 <= xx < 4 and 0 <= yy < 4:
                    if board[xx][yy] != board[sx][sy]:
                        matrix[xx][yy] = matrix[x][y] + 1
                        q.append((xx, yy))

                    elif xx == fx and yy == fy:
                        matrix[xx][yy] = matrix[x][y] + 1
                        shortdict.append([matrix[xx][yy], xx, yy])
                        find = 1
                        break

    print('ctrlmove 추가 최단경로:', shortdict)
    short, fx, fy = min(shortdict)
    board[sx][sy] = 0
    board[fx][fy] = 0
    print(*board, sep='\n')
    return short, fx, fy


def solution(board, r, c):
    move = []

    cards, pair_cards = remain_card(board)
    print(cards, pair_cards)
    kind = list(perm(cards))
    print(kind)
    px, py = r, c

    if board[px][py] != 0:
        kind = list(filter(lambda x: x[0] == board[px][py], kind))
        while cards:
            print('now CARDS:', cards)
            print('x,y', px, py)
            print('포인터가 0인 아닌 경우', kind)
            temp_move = [0] * len(kind)
            temp = board[px][py]
            for i in range(len(kind)):
                print("조합:", kind[i])
                a, b, c = bfs_find_pair(px, py, pair_cards, board)
                temp_move[i] += a
                px, py = b, c
                cards.remove(temp)  # 해당 카드 제거하기

            move.append(min(temp_move))

    else:
        print('포인터가 0인 경우', kind)
        temp_move = [0] * len(kind)

        for i in range(len(kind)):
            a, b, c = bfs_find_card(px, py, kind[i][0], board)
            temp_move[i] += a
            px, py = b, c

            temp = board[px][py]
            cards.remove(temp)  # 해당 카드 제거하기
            print('찾을 카드들', cards)
            a, b, c = bfs_find_pair(px, py, pair_cards, board)
            temp_move[i] += a
            px, py = b, c
        move.append(min(temp_move))

    return move


board1 = [[1, 0, 0, 3], [2, 0, 0, 0], [0, 0, 0, 2], [3, 0, 1, 0]]
board2 = [[3, 0, 0, 2], [0, 0, 1, 0], [0, 1, 0, 0], [2, 0, 0, 3]]

r1, c1 = 1, 0
r2, c2 = 0, 1
print('move:', solution(board1, r1, c1))
print('===============')
# solution(board2, r2, c2)
