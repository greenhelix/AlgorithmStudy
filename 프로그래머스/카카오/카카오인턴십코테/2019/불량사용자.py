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
        if len(kind[i]) != len(bann[i]):  # 아이디 조합의 길이가 다른면 바로 False
            return False
        for j in range(len(kind[i])):  # 각 아이디의 글자를 비교
            if bann[i][j] == '*':  # *부분은 아무 거나 와도 상관없으므로 통과
                continue
            elif bann[i][j] != kind[i][j]:  # 글자가 다른것이 있으면 바로 False
                return False
    return True


def solution(user, bann):
    answer = []
    kinds = list(pm(user, len(bann)))
    # print(kinds)
    for i in kinds:
        if check(i, bann):  # 아이디 조합별로 글자를 비교하여 통과된 경우 해당 아이디 조합을 사용

            i = set(i)  # set으로 변경 - 중복 제거

            if i not in answer:
                print('------')
                print(i)
                answer.append(i)

    print('answer:', answer)
    return len(answer)


print(solution(user, bann))
