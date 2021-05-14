import re
sample1 = "...!@BaT#*..y.abcdefghijklm"
sample2 = "123_.def"


def solution(id):
    answer = ''
    # 3<= id <= 15 , [-, _, .] , . != [-1],[0],repeat
    # lower() -> {\d,-,_,.} -> . * n (n >=2) : . -> [-1] or [0] = . Del -> if Empty : a
    # -> len(id)>=16 : id[:15] -> len(id) <=2 : id[-1]*n if len(id) == 3

    id = id.lower()  # 1단계
    print('1step:', id)
    other = ['-', '_', '.']
    newId = ''
    for i in id:
        if re.compile('\w').match(i):
            newId += i
        if i in other:
            newId += i

    print(id)
    print(newId)
    return answer


solution(sample1)
solution(sample2)
