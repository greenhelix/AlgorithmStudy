def solution(n, computers):
    answer = 0
    search = []
    visit = [0] * n

    while 0 in visit:
        x = visit.index(0)
        search.append(x)
        visit[x] = 1

        while search:
            node = search.pop(0)
            visit[node] = 1
            for i in range(n):
                if visit[i] == 0 and computers[node][i] == 1:
                    search.append(i)
                    visit[i] = i
            answer += 1

    return answer


n = 3
computers = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(n, computers))
