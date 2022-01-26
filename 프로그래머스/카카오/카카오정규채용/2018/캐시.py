# https://programmers.co.kr/learn/courses/30/lessons/17680
# LRU : 캐쉬사이즈에 맞춰 집합을 구성하고 각 데이터를 넣어준다.
# 해당 데이터가 캐쉬집합 안에 없다면, cache miss : 시간이 오래걸린다.
# 해당 데이터가 캐쉬집합 안에 있다면, cache hit :  시간이 짧게걸린다.
# 그리고 캐쉬집합에 데이터가 추가 될때, 정해진 캐쉬사이즈보다 클 경우 맨 앞에 있는 오래된 정보를 pop(0)하고, 추가해준다.

# 이게 바로 LRU 의 개념이다. Least Recently Used Algorithm 가장 오랫동안 참조되지 않은 페이지를 교체한다.
# 페이지 교체 알고리즘(FIFO, LFU, LRU 중 하나) 중 하나이다.
# 프로세스가 주기억장치에 접근할 때마다 참조된 페이지에 대한 시간을 기록해야하므로, 큰 오버헤드(손실)이 발생한다.

cacheSize1, cities1 = 3, ["Jeju", "Pangyo", "Seoul",
                          "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
cacheSize2, cities2 = 3, ["Jeju", "Pangyo", "Seoul",
                          "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
cacheSize3, cities3 = 2, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                          "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cacheSize4, cities4 = 5, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA",
                          "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
cacheSize5, cities5 = 2, ["Jeju", "Pangyo", "NewYork", "newyork"]
cacheSize6, cities6 = 0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]


def solution(cacheSize, cities):

    # 캐쉬가 0인경우는 계속 miss가 뜨기 때문에, 그냥 중복이런거 없다 다 5s씩 추가해주고 리턴시킨다.
    if cacheSize == 0:
        return len(cities)*5

    # 초기 캐쉬와 시작 값을 넣어서 시작한다.
    cache = [cities.pop(0).lower()]
    time = 5

    for i in range(len(cities)):
        print(f'CITY DATA : {cities}')
        temp = cities[0].lower()

        if temp in cache:
            print(f'correct!, {temp} in {cache}>> HIT!')
            time += 1
            cache.remove(temp)
            # cache.append(temp)
            cache.append(cities.pop(0).lower())
            print(f'>>> {cache}, time: {time}\n')

        else:

            if len(cache) == cacheSize:
                del cache[0]
                print(f'FULL CACHE \noldest data delete! {cache}')
            print(f'wrong!, {temp} not in {cache}>> MISS!')
            # cache.append(temp)
            cache.append(cities.pop(0).lower())
            time += 5
            print(f'>>> {cache}, time: {time}\n')

    return time


print(solution(cacheSize1, cities1))
print('============================')
print(solution(cacheSize2, cities2))
print('============================')
print(solution(cacheSize3, cities3))
print('============================')
print(solution(cacheSize4, cities4))
print('============================')
print(solution(cacheSize5, cities5))
print('============================')
print(solution(cacheSize6, cities6))
print('============================')
