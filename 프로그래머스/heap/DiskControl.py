import heapq as hq
from collections import deque


def solution(jobs):
    # sorted에서 key 를 두개의 요소로 하는 이유
    # x[1]의 요소가 다 똑같은 경우에는 x[0]의 기준으로 작은 것 부터 정렬해준다.
    sortJobs = deque(sorted([(x[1], x[0])
                             for x in jobs], key=lambda x: (x[1], x[0])))
    # 대기하는 작업을 넣어주는 공간이다.
    delay = []
    hq.heappush(delay, sortJobs.popleft())
    now, total_time = 0, 0
    while len(delay) > 0:
        # 초기 작업의 시간 계산 및 일반적 순차 작업의 경우 시간 계산해주는 반복문이다.
        amount, start = hq.heappop(delay)
        now = max(now + amount, start + amount)
        total_time += now - start
        # 작업이 대기 중인 경우
        while len(sortJobs) > 0 and sortJobs[0][1] <= now:
            # delay에 넣어주면 자동으로 hq영향을 받아 정렬된다.
            hq.heappush(delay, sortJobs.popleft())
        if len(sortJobs) > 0 and len(delay) == 0:
            hq.heappush(delay, sortJobs.popleft())
    # 나누기를 하는데, 소수점 이하는 버리는 연산자는 // 이다.
    return total_time // len(jobs)


test = [[0, 3], [1, 9], [2, 6]]
sample0 = [[1, 4], [4, 6], [2, 7], [3, 9]]
sample1 = [[1, 4], [1, 6], [1, 7], [1, 9]]
