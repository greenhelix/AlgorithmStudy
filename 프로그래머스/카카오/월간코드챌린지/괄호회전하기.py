from collections import deque
import time


def solution1(s):
    start = time.time()
    answer = 0

    # 회전횟수
    temp = deque(s)
    for i in range(1, len(s)):

        # 올바는 괄호 확인
        a, b, c = 0, 0, 0
        cnt = 0
        print(temp)
        checker = []
        for j in temp:

            ##
            if j in ['(', '{', '[']:
                checker.append(j)
            else:
                if j == ')' and checker.pop() != '(':
                    break
                if j == '}' and checker.pop() != '{':
                    break
                if j == ']' and checker.pop() != '[':
                    break

            if j == '(':
                a += 1
            elif j == ')':
                a -= 1
                if a < 0:
                    print('() error')
                    break
                if a == 0:
                    cnt += 1

            if j == '{':
                b += 1
            elif j == '}':
                b -= 1
                if b < 0:
                    print('{} error')
                    break
                if b == 0:
                    cnt += 1

            if j == '[':
                c += 1
            elif j == ']':
                c -= 1
                if c < 0:
                    print('[] error')
                    break
                if c == 0:
                    cnt += 1

            if cnt == (len(temp)//2):
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
test = "[](){}"
print(solution1(test))
print(solution2(test))
