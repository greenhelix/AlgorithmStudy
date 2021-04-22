# https://programmers.co.kr/learn/courses/30/lessons/67257
from re import split
from itertools import permutations

cal = permutations(['*', '+', '-'])


def solutions(exp):
    answer = 0

    for i in cal:
        print(i)
        nums = split('[*+-]', exp)
        cals = split('[\d]+', exp)[1:-1]
        for j in i[:2]:
            print(nums, cals)
            print('j:', j)
            while j in cals:
                idx = cals.index(j)
                print('idx:', idx)

                sample = nums[idx] + cals[idx] + nums[idx + 1]
                print(sample, '=', eval(sample), '\n')
                nums[idx] = str(eval(sample))
                nums.pop(idx + 1)
                cals.pop(idx)
        sample = ''
        print('.....')
        for z in range(len(cals)):
            sample += nums[z] + cals[z]
        print('계산', sample + nums[-1], '\n')
        sample = abs(eval(sample + nums[-1]))

        if sample > answer:
            answer = sample

    return answer


exp = "50*6-3*2"
print(solutions(exp))

# def solution(exp):
#     answer = 0
#     # 연산 우선순위 조합
#     cal = [['*', '+', '-'], ['*', '-', '+'], ['+', '-', '*'],
#            ['+', '*', '-'], ['-', '+', '*'], ['-', '*', '+']]
#     # 숫자만 추출하여 리스트화

#     nums = list(map(int, re.split('[-*+]', exp)))
#     cals = re.split('[\d]+', exp)[1:-1]
#     print(exp)
#     print(nums, cals)

#     for i in cal:
#         print(i)

#     return answer


# solution(exp)
