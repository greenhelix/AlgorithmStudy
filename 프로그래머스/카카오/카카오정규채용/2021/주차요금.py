from collections import defaultdict
import math


def time_to_min(t):
    h, m = map(int, t.split(':'))
    return (h*60)+m


def calculate(fee, m):
    if m <= fee[0]:
        return fee[1]
    return fee[1] + (math.ceil((m - fee[0]) / fee[2]))*fee[3]


def solution(fees, records):
    answer = []
    park = defaultdict()
    cal_park = dict()

    for i in records:
        time, car, state = map(str, i.split())
        cal_park[car] = 0

    for i in records:
        time, car, state = map(str, i.split())
        print(f'차량번호:{car}\n상태:{state}\n시간:{time}({time_to_min(time)}분)')
        if state == "IN":
            print(f'>>>>>>>>{car}: 주차시작')
            park[car] = time_to_min(time)
            print(park)
        elif state == 'OUT':
            cal_time = time_to_min(time) - park[car]
            print(f'>>>>>>>>{car}: 출차 사용시간{cal_time}')
            cal_park[car] += cal_time
            del park[car]
            print(park)

    if park:
        print('주차중인차량')
        for car, time in park.items():
            print(f'{car}분리하기 {time}')
            t = 1439 - int(time)
            print(f'사용시간 : {t}')
            cal_park[car] += t
    car = sorted(cal_park)
    print(car)
    print(cal_park)

    for i in car:
        answer.append(calculate(fees, cal_park[i]))

    return answer

    fees	records	result


[180, 5000, 10, 600]["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN",
                     "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"][14600, 34400, 5000]
[120, 0, 60, 591]["16:00 3961 IN", "16:00 0202 IN",
                  "18:00 3961 OUT", "18:00 0202 OUT", "23:58 3961 IN"][0, 591]
[1, 461, 1, 10]["00:00 1234 IN"][14841]
