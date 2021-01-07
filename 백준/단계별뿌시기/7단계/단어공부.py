# https://www.acmicpc.net/problem/1157
# 입력되는 문자값에서 가장 빈도가 높은 문자를 대문자로 출력한다.
# 단, 최대 빈도수 문자가 여러개면 ? 를 출력한다.
# Mississipi
# ?
# zZa
# Z
# collections.Counter 예제 (7)
# most_common() 메소드 사용
# import collections
# c2 = collections.Counter('apple, orange, grape')
# print(c2.most_common())
# print(c2.most_common(3))
# '''
# 결과
# [('a', 3), ('p', 3), ('e', 3), ('g', 2), (',', 2), ('r', 2), (' ', 2), ('n', 1), ('l', 1), ('o', 1)]
# [('a', 3), ('p', 3), ('e', 3)]
# '''

import collections

word = collections.Counter(input())
