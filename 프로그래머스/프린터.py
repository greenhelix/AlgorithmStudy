def solution(prior, loc):
    answer = 0
    docs = list([prior[i], i] for i in range(len(prior)))
    wait = []  # 대기목록
    print(docs)
    change = []
    temp = []
    while docs:
        doc = docs.pop(0)
        if wait:
            for i in wait:
                if i[0] < doc[0]:
                    print(f'doc:{doc} wait:{wait}')
                    temp = wait[:]
                    wait = []
                    print(f'temp: {temp}')
                    break

        wait.append(doc)
        print(f'now wait: {wait}')
    print(f'wait: {wait}, temp: {temp}')

    for i in temp:
        wait.append(i)

    print(wait)

    for i in range(len(wait)):
        if wait[i][1] == loc:
            answer = i+1

    return answer


def solutions(prior, loc):
    answer = 0
    docs = list((prior[i], i) for i in range(len(prior)))
    print(docs)

    while docs:
        task = docs.pop(0)
        for i in docs:
            if task[0] < i[0]:
                docs.append(task)
                break
        else:
            answer += 1
            print(f'docs:{docs}')
            if task[1] == loc:
                return answer


p = [2, 1, 3, 2]
pp = [1, 1, 9, 1, 1, 1]
ll = 0
l = 2
# print(solution(p, l))
# print(solution(pp, ll))
print(solutions(pp, ll))
