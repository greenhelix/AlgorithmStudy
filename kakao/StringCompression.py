def solution(s):
    answer = len(s)
    for x in range(1, int(len(s)/2)+1) :
        d = 0 
        comp = ''
        c = 1
        for i in range(0, len(s), x):
            temp = s[i:i+x]
            print(i,') now temp = ',temp, '|now comp = ', comp, '| x = ',x)
            if comp == temp :
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
        answer = min(answer, d)
        print('slice',x,'-->',d," ==========================next")
    return answer

a = 'aabbaccc'
b = "abcabcdede"
print(solution(b))

        