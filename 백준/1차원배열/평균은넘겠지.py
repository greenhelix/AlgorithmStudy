# #  백준 4344번
# 테스트케이스갯수C
# 케이스마다학생의수N이첫수로주어짐.이어서N명의점수가주어짐.
# 각 케이스별 한줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 3자리까지 출력
# print(avr)print(N, score)
C = int(input())
for n in range(C):
    student = list(map(int, input().split()))
    N, score = student[0], student[1:]
    avr = sum(score) / N
    good = 0
    for i in score:
        if i > avr:
            good += 1
    percent = good / N * 100

    print("%0.3f%%" % percent)
