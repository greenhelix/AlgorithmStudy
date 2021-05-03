import sys
sys.setrecursionlimit(10**7)


def check(i, rooms):
    if i not in rooms:
        rooms[i] = i+1
        return i
    find = check(rooms[i], rooms)
    rooms[i] = find + 1
    return find


def solution(k, room_number):
    answer = []
    k_room = dict()
    for i in room_number:
        your = check(i, k_room)
        answer.append(your)

    return answer


k = 10
room_number = [1, 3, 4, 1, 3, 1]

print(solution(k, room_number))
