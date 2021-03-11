def efficientRoadNetwork(n, roads):
    adj = [[] for i in range(n)]
    for rd in roads:
        adj[rd[0]].append(rd[1])
        adj[rd[1]].append(rd[0])
    for city in range(n - 1):
        oneHop = {c for c in adj[city]}
        twoHops = {c for c1 in oneHop for c in adj[c1]}
        if len({city} | oneHop | twoHops) < n:
            return False
    return True

# 비어있는 adj를 선언해준다. 범위는 n으로 설정한다.
# adj에 각 도시별로 길이 나있는데로 저장해준다. 
# n도시 범위내에서 oneHop 한 번에 갈수 있는 것들을 뽑아낸다.
# n도시 범위내에서 twoHop 두 번에 갈수 있는 것들을 뽑아낸다. oneHop으로 한번이동하고 oneHop을 기점으로 또 갈 수 있는 곳을 선정해서 보여준다. 
# if 문을 통해 |비트연산하여 이 oneHop, twoHop의 길이들이 전체 도시의 길이 비트보다 큰지 작은지 판단하는데, 중요한 것은 다른 곳으로 가면 비트가 커진다. 
# 즉,  oneHop 이 3개, twoHop 이 3개 이면, 당시 {city} 는  해당 도시 값이 나올 것이다. 
# 아무튼 이 것들의 | 비트연산을 진행하여 그 길이를 추출하고 n보다 작다면 False를 추출하며 아니면 
# True를 보여주면된다. 