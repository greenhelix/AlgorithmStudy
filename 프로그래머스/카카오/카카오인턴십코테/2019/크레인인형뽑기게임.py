def solution(board, moves):
    answer = 0
    s = []
    for i in moves:
        for j in range(len(board)):
            if board[j][i-1] != 0:
                if len(s) >= 1 and board[j][i-1] == s[-1]:
                    s.pop()
                    answer += 2
                    board[j][i-1] = 0
                    break
                s.append(board[j][i-1])
                board[j][i-1] = 0
                break
    return answer


board = [[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [
    0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]

print(solution(board, moves))
