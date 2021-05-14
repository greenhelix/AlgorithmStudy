from itertools import combinations as comb
sample1, course1 = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]
sample2, course2 = ["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"], [2, 3, 5]
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


print(solution(sample1, course1))
print('========================')
print(solution(sample2, course2))
print('========================')
print(solution(sample3, course3))
