play_time1 = "02:03:55"
adv_time1 = "00:14:15"
logs1 = ["01:20:15-01:45:14", "00:40:31-01:00:00",
         "00:25:50-00:48:29", "01:30:59-01:53:29", "01:37:44-02:02:30"]
play_time2 = "99:59:59"
adv_time2 = "25:00:00"
logs2 = ["69:59:59-89:59:59", "01:00:00-21:00:00",
         "79:59:59-99:59:59", "11:00:00-31:00:00"]
play_time3 = "50:00:00"
adv_time3 = "50:00:00"
logs3 = ["15:36:51-38:21:49", "10:14:18-15:36:51", "38:21:49-42:51:45"]

p = "00:00:20"
a = "00:00:10"
log = ["00:00:02-00:00:06", "00:00:03-00:00:09",
       "00:00:08-00:00:13", "00:00:13-00:00:18"]

# 광고는 재생 중인 동영상의 오른쪽 아래에서 원래 영상과 동시에 재생되는 PIP(Picture in Picture) 형태로 제공
# 공익광고 재생시간은 동영상 재생시간보다 짧거나 같게 주어짐.
# 동적계획법 문제이다.
# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/


def makeSec(time):
    h, m, s = map(int, time.split(':'))
    sec = h*3600 + m*60 + s
    return sec


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    # 모든 시간값을 초로 환산한다.
    play_time_sec = makeSec(play_time)
    adv_time_sec = makeSec(adv_time)
    print(f'총영상시간: {play_time_sec}초, 광고시간: {adv_time_sec}초')
    starts, ends = [], []
    # 각 초별로 0으로 리스트를 만든다.
    total_time = [0 for i in range(play_time_sec + 1)]

    for play in logs:
        start, end = play.split('-')
        start, end = makeSec(start), makeSec(end)
        starts.append(start)
        ends.append(end)
        print(f'시작: {start}초 -> 종료: {end}초')
        # 시작되는 곳과 끝나는 초에 +-1을 각각 주어 중첩의 빈도를 측정한다.
        total_time[start] += 1
        total_time[end] -= 1
    print('0번', total_time)
    # 각 영상로그들의 중첩 빈도를 나타낸다.
    # 영상의 초 단위마다 몇명이 보는지 알 수 있다.
    # 메모이제이션이 진행된다. ( 값을 기억하고 활용한다. )
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]
    print(len(total_time))
    print('1번', total_time)  # 인원이 필요하다면 여기서 멈추고 사용하면 된다.

    # 한번더 반복을 주어 누적 재생시간을 측정한다.
    # 시청자의 명수에 따라 누적 재생시간을 진행하여 볼 수 있다.
    for i in range(1, len(total_time)):
        total_time[i] = total_time[i] + total_time[i - 1]
    print('2번', total_time)

    most_view, max_time = 0, 0

    # 광고초 범위에서 모든 영상 재생 범위로 i를 각 초별로 반복한다.
    for i in range(adv_time_sec - 1, play_time_sec):

        # i가 광고의 전체시간보다 같거나 커진 경우
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
                print('1:::', most_view, max_time)

        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1
                print('2:::', most_view, max_time)

    print(max_time)
    return int_to_str(max_time)


# print(f'{solution(play_time1,adv_time1,logs1)}에 광고 삽입!')
# print('-----------------------------------')
# print(f'{solution(play_time2,adv_time2,logs2)}에 광고 삽입!')
# print('-----------------------------------')
# print(f'{solution(play_time3,adv_time3,logs3)}에 광고 삽입!')
print('-----------------------------------')
print(f'{solution(p,a,log)}에 광고 삽입!')
