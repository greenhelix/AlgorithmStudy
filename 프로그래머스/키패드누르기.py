def distance(q, left, right, hand):
    pad = [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9'], ['*', '0', '#']]
    for i in range(len(pad)):
        for j in range(len(pad[i])):
            if pad[i][j] == q:
                a, b = i, j
            if pad[i][j] == left:
                c, d = i, j
            if pad[i][j] == right:
                e, f = i, j
    print(a, b)
    print(c, d)
    print(e, f)
    l = abs(a - c) + abs(b - d)
    r = abs(a - e) + abs(b - f)
    if l < r:
        return 'L'
    elif l > r:
        return 'R'
    elif l == r:
        return hand[0].upper()


def solution(numbers, hand):
    answer = ''
    lpos, rpos = '*', '#'
    for i in numbers:
        touch = str(i)
        print('now touch:', touch)
        if touch == '1' or touch == '4' or touch == '7':
            answer += 'L'
            lpos = touch
            print('left pos:', lpos)
        elif touch == '3' or touch == '6' or touch == '9':
            answer += 'R'
            rpos = touch
            print('right pos:', rpos)
        elif touch == '2' or touch == '5' or touch == '8' or touch == '0':
            if distance(touch, lpos, rpos, hand) == 'L':
                answer += 'L'
                lpos = touch
            elif distance(touch, lpos, rpos, hand) == 'R':
                answer += 'R'
                rpos = touch

    return answer


# test case
numbers = [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = 'right'

print(solution(numbers, hand))
