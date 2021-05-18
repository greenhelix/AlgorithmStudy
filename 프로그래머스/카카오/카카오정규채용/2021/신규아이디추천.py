import re
sample1 = "...!@BaT#*..y.abcdefghijklm"
sample2 = "123_.def"
sample3 = "z-+.^."
sample4 = '=.='


def startLastCheck(newId):
    if newId[0] == '.' and len(newId) >= 2:  # 4단계
        newId = newId[1:]
    if newId[-1] == '.' and len(newId) >= 2:
        newId = newId[:-1]
    elif newId == '.':
        newId = ''
    return newId

# find, rfind()


def solution(id):

    # 3<= id <= 15 , [-, _, .] , . != [-1],[0],repeat
    # lower() ->
    # {\d,-,_,.} ->
    #  . * n (n >=2) : . ->
    #  [-1] or [0] = . Del ->
    #  if Empty : a ->
    #  len(id)>=16 : id[:15] ->
    #  len(id) <=2 : id[-1]*n if len(id) == 3

    id = id.lower()  # 1단계
    print('1step:', id)
    newId = ''
    for i in id:  # 2단계
        if re.compile('\w').match(i):
            newId += i
        if i in ['-', '.']:
            newId += i
    print('2step:', newId)

    while '..' in newId:  # 3단계
        if '..' in newId:
            newId = newId.replace('..', '.')

    print('3step:', newId)

    newId = startLastCheck(newId)

    print('4step:', newId)

    print('5step:', newId)

    if len(newId) >= 16:  # 6단계
        newId = newId[:15]
        newId = startLastCheck(newId)

    print('6step:', newId)

    if 0 < len(newId) <= 2:  # 7단계
        while len(newId) != 3:
            newId += newId[-1]
    elif len(newId) == 0:
        while len(newId) != 3:
            newId += 'a'

    print('7step:', newId)

    return newId


print(solution(sample1))
print('==')
print  # (solution(sample2))
print('==')
print  # (solution(sample3))
print('==')
print(solution(sample4))
