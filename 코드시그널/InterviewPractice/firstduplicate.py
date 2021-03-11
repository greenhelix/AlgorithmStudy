#주어진 배열, 집합에서 중복되는 숫자들이 발견되면 찾아내는데
#중복 수의 종류 중 가장 처음으로 중복되는 숫자가 무엇인지 리턴해주고 
#중복수가 없다면 -1을 리턴해달라는 문제이다. 

def firstDuplicate(a):
    check = set()
    for i in a :
        if i in check:
            return i 
        check.add(i)
    return -1

sample = [2,1,3,5,3,2]

print(firstDuplicate(sample))