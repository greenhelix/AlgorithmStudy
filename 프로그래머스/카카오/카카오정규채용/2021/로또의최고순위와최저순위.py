# https://programmers.co.kr/learn/courses/30/lessons/77484
def solution(lottos, win_nums):
    answer = []
    cnt, zero = 0, 0
    for i in lottos:
        if i in win_nums:
            cnt += 1
        if i == 0:
            zero += 1

    # 0 숫자가 안 맞은 경우
    a = 7 - cnt

    # 0 숫자가 맞은 경우
    b = 7 - (cnt+zero)

    if a == 7:
        a = 6
    if b == 7:
        b = 6

    answer.append(a)
    answer.append(b)

    return sorted(answer)
