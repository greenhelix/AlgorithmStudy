print({1, 2} & {2})
print({1, 2} | {2})
print(type({1, 2} - {2}))
c = {1, 2} - {2}
print(list(c)[0])

test = "{{1,2,3},{2,1},{1,2,4,3},{2}}"


def solution(s):
    answer = []
    # 문자열을 일단 구분 ['1,2,3', '2,1', '1,2,4,3', '2']
    b = s[2:-2].split('},{')
    # 길이가 짧은 순으로 정렬 ['2', '2,1', '1,2,3', '1,2,4,3']
    b = sorted(b, key=len)
    for i in b:
        # ','로 각 요소를 잘라서 해당 값을 int로 바꾼뒤 list에서 set으로 변경
        # set으로 변경한 이유는 각 값을 비교하기 위해서이며, 이러한 값을 Answer에 넣어준다.
        answer.append(set(list(int(j) for j in i.split(','))))

    # 비교하기위해 일단 무조건 처음값이 될 1번째 값은 미리 넣어준다.
    result = [list(answer[0])[0]]
    # 2번째 요소부터 끝까지 차집함을 통해 남은 하나를 가져와 result에추가해둔다.
    for i in range(1, len(answer)):
        c = answer[i] - answer[i - 1]
        # Set에서는 추출이 불가하므로 list로 변경하여 추출한다.
        result.append(list(c)[0])

    return result


print(solution(test))
