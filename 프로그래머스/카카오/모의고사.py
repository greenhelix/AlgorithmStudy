def solution1(answers):
    pattern = [1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5], [
        3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    l = [5, 8, 10]
    max_cnt = {}

    for i in range(len(l)):
        cnt = 0
        repeat = len(answers) // l[i]
        remain = len(answers) % l[i]
        checker = pattern[i] * repeat + pattern[i][:remain]

        for j in range(len(answers)):
            if answers[j] == checker[j]:
                cnt += 1
        if cnt != 0:
            max_cnt[i+1] = cnt

    return sorted(max_cnt.keys())


def solution2(answers):
    answer = [[1, 0], [2, 0], [3, 0]]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]
    for i in range(3):
        pattern[i] = pattern[i]*(len(answers)//len(pattern[i])) + \
            pattern[i][:(len(answers) % len(pattern[i]))]

    for i in range(len(answers)):
        if answers[i] == pattern[0][i]:
            answer[0][1] += 1
        if answers[i] == pattern[1][i]:
            answer[1][1] += 1
        if answers[i] == pattern[2][i]:
            answer[2][1] += 1

    return list(i[0] for i in sorted(answer, key=lambda x: [-x[1], x[0]]) if i[1] != 0)


def solution3(answers):
    answer = [[0, 1], [0, 2], [0, 3]]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i, v in enumerate(answers):
        if v == pattern[0][i % 5]:
            answer[0][0] += 1
        if v == pattern[1][i % 8]:
            answer[1][0] += 1
        if v == pattern[2][i % 10]:
            answer[2][0] += 1

    print(answer)
    m_value = 0
    while answer:
        t_value = max(answer)
        answer.remove(t_value)
        if t_value[1] >= m_value:
            answer.append(t_value[0])
            m_value = t_value[1]
    return sorted(answer)


def solution4(answers):
    answer = [[1, 0], [2, 0], [3, 0]]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i, v in enumerate(answers):
        if v == pattern[0][i % 5]:
            answer[0][1] += 1
        if v == pattern[1][i % 8]:
            answer[1][1] += 1
        if v == pattern[2][i % 10]:
            answer[2][1] += 1
    print(answer)
    return list(i[0] for i in sorted(answer, key=lambda x: [-x[1], x[0]]) if i[1] != 0)


def solution(answers):
    answer = [[0, 1], [0, 2], [0, 3]]
    pattern = [[1, 2, 3, 4, 5], [2, 1, 2, 3, 2, 4, 2, 5],
               [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]]

    for i, v in enumerate(answers):
        if v == pattern[0][i % 5]:
            answer[0][0] += 1
        if v == pattern[1][i % 8]:
            answer[1][0] += 1
        if v == pattern[2][i % 10]:
            answer[2][0] += 1

    m_value = 0
    result = []

    while answer:
        t_value = max(answer)
        answer.remove(t_value)
        if t_value[0] >= m_value:
            result.append(t_value[1])
            m_value = t_value[0]

    return sorted(result)


test1 = [1, 2, 3, 4, 5]
test2 = [1, 3, 2, 4, 2]
test3 = [3, 3, 3, 4, 5, 1, 1, 1, 3, 4, 5]

# print(solution3(test1))
print(solution3(test3))
