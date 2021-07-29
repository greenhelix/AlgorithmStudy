# https://www.acmicpc.net/problem/1157
# 구현 / 문자열
# 대소문자 단어 in 가장 많이 사용된 알파벳 무엇인가.
# 조건1 대소문자 구분 안함.
# 조건2 출력값은 대문자
# 조건3 가장 많이 사용된 알파벳 여러개이면 ? 출력

word = input().upper()
print(word)
alpha = []
for i in range(65, 91):
    alpha.append(chr(i))
print(alpha)
print(ord('A'))
count = [0] * 26
print(count)
for i in word:
    for j in alpha:
        if i == j:
            count[alpha.index(j)] += 1

print(count)
print(max(count))
isOne = 0
for i in count:
    if max(count) == i:
        isOne += 1

if isOne == 1:
    print('One Max', alpha[count.index(max(count))])
elif isOne > 1:
    print('?')
else:
    print('zero?')

###
# 리스트의 count 메서드를 알았다면 더 빨랐다.
# 그리고 Set을 통해서 중복을 제거해준 상태로 검사했으면 더 빨리 했을듯
# word = input().upper()
# wordCheck = set(word)
# result = ''
# count = 0
# for i in wordCheck:
#     if count < word.count(i):
#         print(i, word.count(i))
#         count = word.count(i)
#         result = i
#     elif count == word.count(i):
#         print(i, 'hey', word.count(i))
#         result = '?'
# print(result)
