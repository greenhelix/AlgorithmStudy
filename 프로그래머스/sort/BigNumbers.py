from itertools import permutations as pm

def solution(numbers):
    answer = ''
    numbers.sort(key= numberHead, reverse=True)
    test2 = {numberHead(i): [value for value in numbers if numberHead(i) == numberHead(value)] for i in numbers}
    print(test2)
    for i, values in test2.items():
        if len(values) == 1:
            answer += str(values[0])
        else:
            answer += pmValue(values)

    return answer
def numberHead(x):
    return x//(10**(len(str(x))-1))
def pmValue(y):
    return max( list (''.join(map(str,i)) for i in list(pm(y, len(y)))))

number1 = [3, 30, 34, 5, 9, 2, 21]
number2 = [6, 10, 2]

print(solution(number1))
#이것은 list of list에서 안쪽 리스트의 순서를 내림차순으로 정렬한다.  = list((sorted(i, reverse=True) for i in group_num))
# print(numbers)
    # test = {i:numberHead(i)  for i in numbers}
    # print(test)
    # group_num = [list(i) for head,i in groupby(list((numberHead(i), i) for i in numbers), lambda x:x[0])]
    # print(group_num)
    # for i in group_num :
    #     if len(i) == 1:
    #         answer += str(i[0][1])
    #     else :
    #         change_position =  {value:h for h, value in i}
    #         mix_value = list(change_position.keys())
    #         answer += pmValue(mix_value)