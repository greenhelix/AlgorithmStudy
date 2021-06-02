from collections import deque
import time


def solution1(s):
    start = time.time()
    answer = 0
    temp = deque(s)

    # 회전횟수
    for i in range(1, len(s)):

        # 올바는 괄호 확인
        cnt = 0
        checker = []
        for j in temp:

            ##
            if j in ['(', '{', '[']:
                checker.append(j)

            else:
                if not checker:
                    break
                check = checker.pop()

                if j == ')':
                    if check == '(':
                        cnt += 1
                    else:
                        break
                if j == '}':
                    if check == '{':
                        cnt += 1
                    else:
                        break

                if j == ']':
                    if check == '[':
                        cnt += 1
                    else:
                        break

            if cnt == (len(temp) // 2):
                answer += 1

        # 회전
        temp.rotate(-1)

    return print(answer, '\n속도:', time.time() - start)


def check(s):
    isTrue = []

    for i in s:
        if i in ['(', '{', '[']:
            isTrue.append(i)

        else:
            # 아무것도 없다면
            if not isTrue:
                return False
            balance = isTrue.pop()
            if i == ')' and balance != '(':
                return False
            if i == '}' and balance != '{':
                return False
            if i == ']' and balance != '[':
                return False

    # 남은게 있다면,
    if isTrue:
        return False
    return True


def solution2(s):
    start = time.time()
    answer = 0
    for i in range(len(s)):
        temp = deque(s)
        temp.rotate(-i)
        if check(temp):
            print(temp)
            answer += 1

    return print(answer, '\n속도:', time.time() - start)


# 예제 테스트는 통과했으나 제출 시 시간초과 발생
test, test1, test2, test3, test4 = "[](){}", "}]()[{", "{{{{{{{", "({[]}){{}}", "}}]]))(([[{{"
print(solution1(test3))
print(solution2(test3))

print(solution1(test4))
print(solution2(test4))
# print(solution1(test))
# print(solution2(test))
# print(solution1(test1))
# print(solution2(test1))
# print(solution1(test2))
# print(solution2(test2))
