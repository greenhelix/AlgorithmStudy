# import re
# from itertools import permutations as pm
# from itertools import combinations as cb
# sample = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
# test1, test2, test3 = set(), set(), set()
# test4, test5, test6 = [], [], []

# for i in sample:
#     m = re.match('[\w]rodo', i)
#     if m:

#         test1.add(m.group())
#         test4.append(m.group())
# for i in sample:
#     m = re.match('[\w]rodo', i)
#     if m:

#         test2.add(m.group())
#         test5.append(m.group())
# for i in sample:
#     m = re.match('[\w][\w][\w][\w][\w][\w]', i)
#     if m:

#         test3.add(m.group())
#         test6.append(m.group())
# print(test1)
# print(test2)
# print(test3)
# result = test1 | test2 | test3
# print(result)
# ====================================================================

# 정규식보다 반복문으로 푸는 경우가 많았다. 사용자 아이디에서 금지된 아이디 목록의 길이로
# 경우의 수를 만들어서 일단 이것들이 금지된 아이디와 일치하는지 일일히 검사를 한뒤
# 일치하면 Set으로 중복을 제거한뒤 answer에 추가해서 모든 경우의 수를 추출 한다.

from itertools import permutations as pm
user = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
bann = ["fr*d*", "*rodo", "******", "******"]


def check(kind, bann):
    for i in range(len(kind)):
        if len(kind[i]) != len(bann[i]):
            return False
        for j in range(len(kind[i])):
            if bann[i][j] == '*':
                continue
            elif bann[i][j] != kind[i][j]:
                return False
    return True


def solution(user, bann):
    answer = []
    kinds = list(pm(user, len(bann)))
    for i in kinds:
        if check(i, bann):
            i = set(i)

            if i not in answer:
                print(i)
                answer.append(i)

    return len(answer)


print(solution(user, bann))
