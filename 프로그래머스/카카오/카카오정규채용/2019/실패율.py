from collections import Counter as cnt

# 사천성 단계별로 유저들의 현재 단계를 준다. [2, 1, 2, 6, 2, 4, 3, 3]
# 유저의 수는 1명이상 20만명 이하이다.
# 현재 나온 단계는 n 이다.(1<= n <= 500)
# 각 단계별로 실패율을 계산하여, 실패율이 높은 순으로 내림차순으로 단계를 보여줘라
# 실패율 = n스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / n스테이지에 도달한 플레이어 수
# 단, n+1 단계에 있는 유저는 모든 단계를 마친 상태이므로 실패율을 0으로 계산해야 한다.


def solution(n, fares):
    answer = []

    # counter를 사용해서 각 단계에 멈춰있는 사용자 수를 센다.
    # [[1, 1], [2, 3], [3, 2], [4, 1], [6, 1]]
    # 1단계 1명, 2단계 3명 ....이런식으로 저장한다.
    now = sorted([[k, v] for k, v in cnt(fares).items()])
    print(now)

    # 위의 배열을 단계와 멈춘 유저수 리스트로 나눠준다.
    # (이 부분을 한번에 가능하게 할 수 없나 싶네요.)
    # 이렇게 나누는 이유는 각 유저들의 단계별 인원수에 맞춰 인덱스를 사용하기 위함입니다.
    현재단계, 멈춘유저수 = [], []

    for i in now:
        현재단계.append(i[0])
        멈춘유저수.append(i[1])
    print(f'현재단계:{현재단계}')
    print(f'멈춘유저:{멈춘유저수}')

    # 실패율 계산 부분
    temp = []

    # 1단계부터 n+1 단계를 기준으로 반복을 시작합니다.
    for stage in range(1, n + 1):

        # 그리고 유저들의 현재 단계에 맞춰 일치하는 부분을 찾기 위해 반복을 돌립니다.
        for s in range(len(현재단계)):

            # stage에서 멈춘 유저가 없는 경우
            if 현재단계[s] > stage:
                ratio = 0.0
                print(f'****{stage}단계****\n{멈춘유저수[s]}명의 유저만 넘어감')
                print(f'{sum(멈춘유저수[:s])}명은 가지도 못했다.')
                print(f'{stage}단계->실패율:{ratio}')
                temp.append([ratio, stage])
                break

            # stage에서 멈춘 유저가 있는 경우
            elif 현재단계[s] == stage:
                ratio = 멈춘유저수[s] / sum(멈춘유저수[s:])
                print(f'****{stage}단계****\n{sum(멈춘유저수[:s+1])}명의 유저가 아직 클리어 못함')
                print(f'{stage}단계->실패율:{ratio}')
                temp.append([ratio, stage])
                break

    print(temp)
    # sorted 안의 list의 요소들별 나열 방식을 설정하는 방법
    # sorted에서 lambda를 사용하여 원하는 대로 나열을 하게 하였다.
    # [[]] 이중리스트 이므로 이런식으로 구성해주고,
    # -x[0]: 1번째 인자를 기준으로 내림차순으로 정렬하고,
    # x[1]: 1번째 인자가 같다면, 2번째 인자를 기준으로 오름차순으로 정렬한다.
    print(*sorted(temp, key=lambda x: [-x[0], x[1]]), sep='\n')

    # 잘 정렬된, temp에서 원하는 값인 스테이지 순을 Answer에 추가해준다.
    for i in sorted(temp, key=lambda x: [-x[0], x[1]]):
        answer.append(i[1])

    # 아무도 도달한적이 없는 스테이지의 경우가 측정이 안된다.
    # 반복문을 통해 아무도 도달하지 않은 단계는
    for c in range(1, n+1):
        if c not in answer:
            print(f'{c}단계가 없다. 추가한다.')
            answer.append(c)

    return answer


def solution2(N, stages):
    stages.sort()  # 기본 각 유저들의 위치를 정렬
    p = len(stages)  # 유저의 총 명수를 p로 선언
    answer = []
    for i in range(1, N+1):  # 간 단계별로 반복문
        t = stages.count(i)  # 각 스테이지별 카운트를 t에 담는다.

        if t == 0:  # 아무도 도달하지 못한 경우의 스테이지 경우
            answer.append((i, 0))  # 답안에 해당 스테이지, 0실패율로 입력
        else:
            answer.append((i, t/p))  # 그 외의 경우는 해당 스테이지의 인원수/현재유저수로 실패율을 계산한다.
        p = p - t  # 실패율 계산이 진행됐으므로, 유저수를 줄여준다.
    answer.sort(key=lambda x: (-x[1], x[0]))  # 정렬을 통해서 원하는 형식으로 정렬한다.
    return [x for x, y in answer]


def solution3(n, stages):
    stages.sort()
    user_num = len(stages)
    print(stages, user_num)

    answer = []

    for i in range(1, n + 1):
        now_user = stages.count(i)
        print(i, '::', now_user)
        if now_user == 0:
            answer.append((i, 0))
        else:
            answer.append((i, now_user / user_num))

        user_num -= now_user

    print(answer)
    answer.sort(key=lambda x: (-x[1], x[0]))
    print(answer)
    return [x for x, y in answer]


n = 5
n1 = 4
n2 = 5
n3 = 5
fare = [2, 1, 2, 4, 2, 4, 3, 3]
fare1 = [4, 4, 4, 4, 4]
fare2 = [1, 2, 3, 4, 2, 2, 3, 4]
fare3 = [1, 2, 3, 1, 2, 1, 2, 1]
# print(solution(n, fare))
# print("============")
# print(solution(n1, fare1))
# print("============")
print(solution3(n, fare))
print("============")
print(solution3(n1, fare1))
# print("============")
# print(solution(n2, fare2))
# print("============")
# print(solution(n3, fare3))
