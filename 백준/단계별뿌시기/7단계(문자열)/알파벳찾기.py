# https://www.acmicpc.net/problem/10809
# 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서,
# 단어에 포함되어 있는 경우에는 처음 등장하는 위치를,
# 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.
# https://www.geeksforgeeks.org/python-ways-to-remove-duplicates-from-list/
# 전체알파벳순으로인덱스가들어있다.
# 단어를검사해서, 해당알파벳인덱스에단어안에인덱스번호로바꿔준다.
# 만약 알파벳순으로 봤을때, 해당 글자가 없다면 -1로 바꿔준다.
# 중복된 알파벳은 처음 나온 알파벳의 인덱스로 해준다.

# 세번째 방법 / 사고의 개념만 바꾸면 된다.
# 반복문의 기준을 알파벳으로 둬서 메모리의 소모가 늘어났다.
# 즉, 입력되는 단어의 길이에 맞춰서 반복문을 돌렸어야 했다.
alphabet = [-1] * 26
word = input()
for i in range(len(word)):
    if alphabet[ord(word[i]) - 97] == -1:
        alphabet[ord(word[i]) - 97] = i
print(*alphabet)

# 첫번째 방법 정담은 나오는데, 런타임 에러
# alphbet = [-1] * 26  # 알파벳수만큼 -1을 먼저 깔아준다.
# word = list(input())  # 입력값을 리스트로 받아준다.(중복허용, 순서있음)
# checkWord = []  # 중복을 제거해준 리스트를 또만든다.
# [checkWord.append(x) for x in word if x not in checkWord]
# for i in checkWord:
#     for j in range(len(alphbet)):
#         if j == (int(ord(i)) - 97):
#             alphbet[j] = int(word.index(i))

# print(*alphbet)  # 출력

# # 두번째 방법 정답은 나오는데, 틀렸음  런타임에러
# two = [-1] * 26
# words = [x-97 for x in list(map(ord, input()))]
# print(word)
# for i in range(len(two)):
#     if i in word and two[i] == -1:
#         two[i] = word.index(i)

# print(" ".join(map(str, two)))
