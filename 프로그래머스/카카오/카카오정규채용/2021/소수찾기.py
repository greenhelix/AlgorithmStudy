# 437674, 3
# 기댓값 〉	3
# 실행 결과 〉	테스트를 통과하였습니다.
# 출력 〉	211020101011

# 	110011, 10
# 기댓값 〉	2
# 실행 결과 〉	테스트를 통과하였습니다.
# 출력 〉	110011
def tentoN(num, n):
    n_dic = {0: '0', 1: '1', 2: '2',
             3: '3', 4: '4', 5: '5',
             6: '6', 7: '7', 8: '8',
             9: '9', 10: 'A', 11: 'B',
             12: 'C', 13: 'D', 14: 'E', 15: 'A'}
    result = ''
    q, r = divmod(num, n)
    while q > 0:
        result = n_dic[r] + result
        q, r = divmod(q, n)

    result = n_dic[r] + result
    print(result)
    return result


def prime_check(x):
    if x == '1':
        return False
    for i in range(2, int(x)):

        if int(x) % i == 0:
            return False
    return True


def solution(n, k):
    answer = 0
    check = list(tentoN(n, k).split('0'))
    for i in check:
        if i == '':
            continue
        if prime_check(i):
            answer += 1
    return answer
