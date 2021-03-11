from itertools import permutations
import copy
def roadsBuilding(cities, roads):
    city = [i for i in range(cities)]
    result = []
    whole_roads = set(permutations(city, 2))
    reverse_roads =copy.deepcopy(roads)
    for i in range(len(roads)) :
        reverse_roads[i][0] = roads[i][1]
        reverse_roads[i][1] = roads[i][0]     
    last_roads = list(whole_roads - set(tuple(a) for a in roads) - set(tuple(b) for b in reverse_roads))
    for i in range(len(last_roads)):
        if last_roads[i][0] < last_roads[i][1] : result.append(list(last_roads[i]))
   
    result.sort(key=lambda e: (e[0], e[1]))
    return  result
# whole_road = list(map(list,permutations(city, 2)))
# 전체적인 도로의 종류를 다 담앗다. 중복을 없애려면, Combinations를 사용한다.
#이미있는 길들의 이름을 거꾸로 표현한것도 따로 만들었다. 이부분을 간단하게 하고 싶다.
# 여기까지하면, 결과는 나오는데, 정렬이 안된상태.