import calendar
def websiteCalender(month, year):
    return calendar.HTMLCalendar().formatmonth(theyear = year, themonth = month, withyear = True).replace("\n","")
    #calendar 모듈 함수를 통해서 fromatmonth()함수를 불러들여, year, month를 설정해주면 해당 연도의 달 날짜와 요일이 나온다. 
    # replace는 문제의 요구사항에서 \n 을 빈칸으로 해달라했기 때문에 생략할 수 있게 한다. 

testM = 8
testY = 2020

print(websiteCalender(testM, testY))