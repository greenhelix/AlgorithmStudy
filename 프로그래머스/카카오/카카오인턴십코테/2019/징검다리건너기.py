def mysolution(stones, k):
    answer = 0
    go = 1
    print(stones)
    while(go):
        j = 0

        for i in range(len(stones)):
            if i == len(stones):
                break
            if j == k:
                go = 0
                return answer
            if stones[i] == 0:
                j += 1
                stones[i] = 0
            else:
                stones[i] -= 1
                j = 0

        print('complete', answer + 1, 'people')
        print(stones)
        answer += 1
    return answer


st = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3

print(mysolution(st, k), '명 건너기완료.')

# 이분 탐색으로 진행해야 한다.


def calc(stones, k, mid):  # 건널 수 있는지를 체크 하는 것
    now = 0
    for stone in stones:
        if(stone < mid):
            # stone - mid 가 0이면 이번 회엔 건널 수 있다는 것임
            now += 1
            # 즉 stone < mid 이면 전 사람 건널 때 0이 되어서 못 건너게 됐다는 것.
            # 건너 뛰는 것 값을 + 1 해준다.
        else:   # 연속으로 나온게 아니면 다시 0으로 만들어줌.
            now = 0
        if(now >= k):  # now가 k랑 같거나 커지면 못 건너는 것.
            return False
    return True


def solution(stones, k):
    left = 1  # 최소 1명은 건널 수 있기 때문에
    right = max(stones) + 1
    # 최고 값 + 1, 그래야 두개 더해서 // 할 때 내림을 하게 되기 때문에 제대로 됨.
    while(left < right - 1):  # 1차이 날 땐 더이상 가운데가 없기 때문에 left쪽이 답/ right에 넣는 mid는 불가능한 값으로 측정 되어있음
        mid = (left + right) // 2  # 중간의 값 정수가 나오게
        if(calc(stones, k, mid)):  # mid가 가능한지 확인
            left = mid
        else:
            right = mid

    return left


print(solution(st, k), '명 건너기완료.')
