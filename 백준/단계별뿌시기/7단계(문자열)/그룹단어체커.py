# https://www.acmicpc.net/problem/1316
# 구현 / 문자열
case = int(input())
count = 0
for i in range(case):
    word = input()
    for j in range(len(word)):
        if j != len(word)-1:
            if word[j] == word[j + 1]:
                pass
            elif word[j] in word[j + 1:]:
                break
        else:
            count += 1

print(count)
