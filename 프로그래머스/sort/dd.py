from itertools import groupby, permutations as pm

def solution(numbers):
    answer = ''
    numbers.sort(key= numberHead, reverse=True)
    group_num = [list(i) for head,i in groupby(list((numberHead(i), i) for i in numbers), lambda x:x[0])]  
    
    for i in group_num :
        if len(i) == 1:
            answer += str(i[0][1])
        else :
            change_position =  {value:h for h, value in i}
            mix_value = list(change_position.keys())
            answer += pmValue(mix_value)
    return answer
def numberHead(x):
    return x//(10**(len(str(x))-1))
def pmValue(y):
    return max( list (''.join(map(str,i)) for i in list(pm(y, len(y)))))