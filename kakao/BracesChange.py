def balanced(p):
    num, tmep = 0, []
    # 균형이 발견된 부분부터의 인덱스를 구하는 함수이다. 
    for idx, value in enumerate(p):
        if value == ")": num -= 1
        if value == "(": num += 1
        if num == 0: 
            return idx
# 단순히 이미 완벽한 ()구성인지 확인하는 함수이다.
def is_right(string):
    temp =[]
    for i in string:
        #시작은 ( 으로 되기 때문에 ( 가 보이면 temp에 넣어준다.
        if i == "(":
            temp.append(i)
        else:
            #중간에 이미 temp가 다 없어진 경우 이미 불균형이라 바로 False리턴한다.
            if len(temp) == 0:
                return False
            # )가 나온다면, 그냥 pop을 해서 temp에 들어 있던 ( 을 빼준다. 
            # 이 작업이 대칭인지 아닌지를 판단해주는 부분이다. 
            temp.pop()
    
    #만약 한 쪽이라도 (,) 더 많은 경우 균형이 있을 수 없으므로 False를 리턴한다. 
    if len(temp) != 0:
        return False
    return True

def solution(p):
    #기본적으로 균형인지 아니면 아무것도 없는지 걸러준다.
    if p =="" or is_right(p):
        print('clear', p)
        return p
    print('this',p ,' test balance? ', is_right(p), 'lets start')
    #balanced에서 구한 인덱스 값을 활용해서 둘로 나눈다.
    u, v = p[:balanced(p)+1], p[balanced(p)+1:]
    print('so u, v', u, '  ', v)
    # 자른 부분 u가 균형있을 때는 이쪽으로 보내서 재귀적으로 solution
    # 하여 v를 다시 잘라본다.
    if is_right(u):
        print('oh!!!!here?  u>> ', u)
        string = solution(v)
        print('so string= ', string)
        #최종적으로 나왔을때, 원래 u랑 string을 더해준다.
        return u+string
    
    # 균형이 안잡힌 부분이 실제로 교정되는 부분이다. 
    # 단순히 ( )을 서로 바꿔주기만하면되는데, 재귀를 통해서 만들어낸다.
    else:
        print('fit v = ',v)
        t = "("
        t += solution(v)
        t += ")"
        print('now t = ',t)
        #실제적으로 u 부분의 1:-1 부분만 가져다 쓰는데, 
        print(u,'>>>')
        u = list(u[1:-1])
        print(u)

        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ")"
            elif u[i] == ")":
                u[i] ="("
        print(u,'perfect!')
        t += "".join(u)
        print('join u>> ' , t)
        return t

test = ")("
test2 = "(()())()"
test3 = "()))((()"
test4 = "))(())(("
print(solution(test3))
print('--------------------')
print(solution(test4))