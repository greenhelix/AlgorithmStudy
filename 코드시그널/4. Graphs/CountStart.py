# 순환되지 않은 상태의 노드들의 연결 부분들을 별이라 한다.
# 이러한 별들의 갯수를 리턴하라.

def countStars(adj):
    star = 0
    night = {i: [] for i in range(len(adj))}

    # T/F로 구성된 맵을 딕셔너리로 변환한다.
    for i in range(len(adj)):
        for j in range(len(adj)):
            if adj[i][j]:
                night[i].append(j)
    print(night)

    for k, v in night.items():
        if len(v) >= 2:  # 도착 노드가 2 이상인 곳은 반복을 통해 별인지 아닌지 확인한다.
            temp = 0
            for check in v:
                if len(night[check]) == 1:
                    temp += 1  # 도착노드가 길이 오직 하나인경우는 카운트
                if temp == len(v):
                    star += 1  # 모두 도착노드까지의 길이 하나이면 스타이므로 별을 늘려준다.
                    # 그외의 순환되는 경우는 별이 아니다.
        if len(v) == 1:
            find = v[0]  # 도착 노드가 한 개인 경우는 양 쪽다 한 개여야 별이 된다.
            if find == k:  # 노드 스스로를 도착지라고 하는 경우도 있어서 이것은 별이 아니다.
                star -= 1
            if len(night[find]) == 1:
                star += 1
                night[find] = []  # 도착 노드의 노드 정보를 없애줘야 중복 카운트를 하지 않는다.

    return star


def otherStar(adj):
    n = len(adj)
    # sum()은 t/f 집합에 적용하면 true값을 1로 합쳐서 보여준다.
    # 이러한 인접행렬을 표현할 때 간편하겠다.
    s = [sum(i) for i in adj]
    star = 0
    print(s)

    for i in range(n):
        # Generator 표현식을 사용하였다.
        # 지연평가 구현체로서 원하는 경우만 계산을 하여 보여준다.
        if adj[i][i] == False and all(s[j] == 1 for j in range(n) if adj[i][j]):
            print(list(s[j] == 1 for j in range(n) if adj[i][j]), s[i])
            star += 1 if s[i] > 1 else 0.5*s[i]
    return int(star)


adj = [[False, True, False, False, False],
       [True, False, False, False, False],
       [False, False, False, True, False],
       [False, False, True, False, False],
       [False, False, False, False, False]]

adj2 = [[False, True, True, True, True, True, True, True],
        [True, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False],
        [True, False, False, False, False, False, False, False]]

print(countStars(adj))
print(countStars(adj2))
print(otherStar(adj))
print(otherStar(adj2))
print("==========")
test = [True, False, False, False, False, False, False, False]
print(sum(test))
