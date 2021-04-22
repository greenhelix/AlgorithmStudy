def find(start, jewl: list()):
    address, re, count = [], [], set()
    kind = list(set(jewl))
    print('kind::', kind)
    if len(kind) == 1:
        return [1], [1, 1]
    checker = [i for i in range(len(kind))]

    for i in range(start, len(jewl)):

        for j in range(len(kind)):
            if jewl[i] == kind[j]:
                if j in checker:
                    re.append(j)
                    count.add(j)
                    address.append(i+1)

        if count == set(checker):
            addr = [address[0], address[-1]]

            return re, addr

    return [0], [0]


def solution(gems):
    answer, answer2, real = [], [], []
    finalanswer = []
    print('gems::', gems)
    for i in range(len(gems)):
        result, addr = find(i, gems)

        if result == [0]:
            break
        answer2.append(addr)
        answer.append(result)

    print('*******************')
    finanswer = min(list(sum(i) for i in answer))
    for i in range(len(answer)):
        if finanswer == sum(answer[i]):
            real.append(i)

    if len(real) > 1:
        real = sorted(real)
        finalanswer = answer2[real[0]]
    else:
        finalanswer = answer2[real[0]]

    return finalanswer


j = ["XYZ", "XYZ", "XYZ"]
print(solution(j))
# ===================================================================

# 딕셔너리를 활용해서 풀어야 한다.
# 각 좌표를 처음 위치로 잡고, 보물의 종류만큼 구성되면 해당 좌표를 최신화 한다.
# 반복하기 위해 해당 위치의 좌표들을 +1 함으로써 계속 다음 번째 보석들에서 시작하여
# 검색을하고 이러한 사이 거리가 처음 부터 끝까지 거리보다 작은 경우
# 해당 거리를 최신화시키고, 이중 점점 제일 작은 거리의 값을 구한다.


def solutions(gems):
    size = len(set(gems))
    dic = {gems[0]: 1}
    temp = [0, len(gems) - 1]
    start, end = 0, 0

    while(start < len(gems) and end < len(gems)):  # 최대치보다 커지면 종료된다.
        if len(dic) == size:
            if end - start < temp[1] - temp[0]:  # 거리를 측정하여 최소값으로 만드는 조건문
                temp = [start, end]  # 젤 작은것으로 temp를 최신화시킨다.
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1

        else:
            end += 1
            if end == len(gems):
                break
            if gems[end] in dic.keys():
                dic[gems[end]] += 1
            else:
                dic[gems[end]] = 1

    return [temp[0]+1, temp[1]+1]
