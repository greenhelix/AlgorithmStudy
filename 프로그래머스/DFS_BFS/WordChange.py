from collections import deque as queue


def trans(a, b): return sum((1 if x != y else 0) for x, y in zip(a, b)) == 1
# trans  = lambda a, b : sum((1 if x!= y else 0) for x, y in zip(a, b)) == 1


def solution(begin, target, words):
    q, d = queue(), dict()
    q.append((begin, 0))
    d[begin] = set(filter(lambda x: trans(x, begin), words))
    print('deque q = > ', q)
    print('frist dict d = > ', d, 'begin과 비슷한 것을 먼저 찾아서 넣어준다.')
    for w in words:
        d[w] = set(filter(lambda x: trans(x, w), words))
    print('dict d = > ', d)
    while q:
        cur, level = q.popleft()
        print('================================')
        print('cur = ', cur, ' level= ', level)
        if level > len(words):
            return 0
        for w in d[cur]:
            print('testing...', w)
            if w == target:
                return level + 1
            else:
                q.append((w, level + 1))
            print('now q = ', q)

    return 0


start = 'hit'
t = 'cog'
words = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(start, t, words))
