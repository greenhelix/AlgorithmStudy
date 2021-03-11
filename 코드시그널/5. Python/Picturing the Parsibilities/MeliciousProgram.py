import datetime
#이 문제는 curDate에서 chnages부분이 각 위치의 값을 더하여 조정된 날짜를 출력해달라는 것이다.
def maliciousProgram(curDate, changes):
    # strptime은 해당 시간과 패턴을 파라미터로 받는다. // datetime.strptime(date_string, format)
    #'%d %b %Y %H:%M:%S' 이부분은 패턴이다. 
    time = datetime.datetime.strptime(curDate, '%d %b %Y %H:%M:%S')
    print(time) # 2016-07-01 16:53:24 그냥 이렇게 출력됨.
    # changes의 리스트를 각 해당 위치 단어로 대체한다.
    d, m, y, H, M, S = changes
    try:
        # newtime에 각 포지션별로, 위의 리스트 변수값들을 더해준다. 
        newtime = time.replace(year=time.year+y,
        month = time.month+m,
        day = time.day+d,
        hour = time.hour+H,
        minute = time.minute+M,
        second = time.second+S)
    except ValueError:
        return curDate
    #마지막에 strtime을 통해서 출력을 원하는 형태로 출력되게 조정해준다.  
    print(newtime) #2015-10-03 16:58:28 이 상태에서 변형주면된다. 
    return newtime.strftime('%d %b %Y %H:%M:%S')


curDate = "01 Jul 2016 16:53:24"
changes = [2, 3, -1, 0, 5, 4]

print(maliciousProgram(curDate, changes))