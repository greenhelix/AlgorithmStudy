# from collections import Counter
p = ['a', 'b', 'c', 'a']
c = ['a', 'b', 'c']


# def solution(participant, completion):
#     return print(list((Counter(participant) - Counter(completion)).elements())[0])


def ssolution(participant, completion):
    answer = ''
    part = tuple(participant)
    com = tuple(completion)
    res = list(a for a in part)
    print(res)
    for i in com:
        if i in part:
            list(res).remove(i)

    answer = res[0]
    return print(answer)


ssolution(p, c)
# solution(p, c)
