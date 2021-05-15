from itertools import combinations as comb
from collections import Counter as cnt

sample1, course1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
sample2, course2 = ["ABCDE", "ABCDE", "AB",
                    "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
sample3, course3 = ["XYZ", "XWY", "WXA"], [2, 3, 4]

# 코스요리
# orders : 손님들이 주문했던 음식 조합
# course : 주인이 만들고 싶은 단품메뉴들의 갯수가 담긴 배열이다.


def solution(orders, course):
    answer = []
    menu = []

    for i in orders:  # 메뉴판을 만든다.
        menu += list(i)
    menu = sorted(set(menu))
    print('menu:', menu)

    temp = []
    for i in course:
        temp = list(comb(menu, i))
        # print(f'{i}가지 코스조합: {temp}')
        count = [0]*len(temp)

        for check in orders:
            for j in range(len(temp)):
                cnt = 0
                for k in range(len(temp[j])):
                    if temp[j][k] in list(check):
                        cnt += 1
                    if cnt == len(temp[j]):
                        count[j] += 1

        # print(i, ':', count)
        max_count = max(count)
        for m in range(len(count)):
            if max_count == count[m] and max_count > 1:
                answer.append(temp[m])
    # print(answer)
    return sorted(list(map(''.join, answer)))


def solution2(orders, course):
    answer = []

    for k in course:
        kind = cnt()
        for order in orders:
            if len(order) >= k:
                temp = [''.join(sorted(c)) for c in comb(order, k)]
                menu = cnt(temp)
                kind += menu
                if kind == cnt():
                    print('here1')
                    break
        if kind == cnt():
            print('here2')
            break
        print(kind)

        m = max(kind.values())

        for i, v in kind.items():
            if m == v and m > 1:
                answer.append(i)

    print('**********************')

    return sorted(answer)


# print(solution(sample1, course1))
# print('========================')
# print(solution(sample2, course2))
# print('========================')
# print(solution(sample3, course3))
print(solution2(sample1, course1))
print('========================')
print(solution2(sample2, course2))
print('========================')
print(solution2(sample3, course3))
