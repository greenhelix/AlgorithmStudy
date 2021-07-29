n = 10
cards = [6, 3, 2, 10, 10, 10, -10, -10, 7, 3]
m = 8
holds = [10, 9, -5, 2, 3, 4, 5, -10]
# 이분탐색은 반드시 정렬을 한 상태로 진행 한다.

# [3, 0, 0, 1, 2, 0, 0, 2]


def binary_search(num, cards):  # 이분 탐색의 기본 수도 코드
    cnt = 0
    if cards[0] == num:
        for i in cards:
            if i == num:
                cnt += 1

    mid = len(cards) // 2
    if num > cards[mid]:
        return binary_search(num, cards[:mid])
    else:
        return binary_search(num, cards[mid:])
