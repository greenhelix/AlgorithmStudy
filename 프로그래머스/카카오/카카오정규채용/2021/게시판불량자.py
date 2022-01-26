def solution(id_list, report, k):
    answer = {a: 0 for a in id_list}
    ban_list = {a: set() for a in id_list}

    for i in report:
        a, b = map(str, i.split())
        if b in ban_list:
            ban_list[b].add(a)

    for i, v in ban_list.items():
        if len(v) >= k:
            for j in v:
                answer[j] += 1

    return list(answer.values())


["muzi", "frodo", "apeach", "neo"]
["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"],
[2, 1, 1, 0]
