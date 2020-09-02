#문자열 압축 문제.
def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1) :
        #문자열s의 반을 범위로 x가 들어가는데, 여기서 X는 압축단위로 활용된다.
        d = 0 
        comp = ''
        c = 1
        #x의 값대로 각 글자들을 i에 인덱스로 보낸다.
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            print(i,') now temp = ',temp, '|now comp = ', comp, '| x = ',x)
            if comp == temp :
                #c는 count이다. 앞의 comp와 temp가 같다면 카운트 해주는 조건문이다.
                c+=1
                print('>>>same!!! now c = ', c)
            elif comp != temp:
                d += len(temp)
                print('now d = ', d)
                if c > 1:
                    d+= len(str(c))
                    print('c>1 so...d = ', d)
                c = 1
                print('d = ', d, ' c reset ', c)
                comp = temp
                print(i,') change>>>> comp = ', comp, '| x = ',x)
        if c>1:
            d += len(str(c))
        print('answer =>',answer)
        print('d =>',d)
        answer = min(answer, d)
        print('slice',x,'-->',answer," ==========================next")
    # 따로 압축된 문자열을 뽑을 수는 없다. 
    # 왜냐하면, 이 코드는 c, d 로 카운트 해가면서 숫자를 세는 코드이기 때문이다. 
    # 반복문을 통해 min()으로 1글자로 묶을때, 2글자로 묶을때의 전체 길이수를 비교하여 
    # 최고로 작은 값을 리턴할 수 있게 하는 원리이다. 
    return answer

#이런 문제를 보면, 압축에 대한 문자열의 길이와 
a = 'aabbaccc'
b = "abcabcdede"
print(solution(a))