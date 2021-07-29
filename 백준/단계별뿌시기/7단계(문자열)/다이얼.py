# https://www.acmicpc.net/problem/5622
# 구현
# 대문자 알파벳 IN -- 알파벳 숫자로 변환 -- 숫자 단위별 시간 값 계산 -- 최소 시간 OUT
# 조건1 ) 숫자 1 - 2s , 2 - 3s ... 식이다. 알파벳 ABC -2 , DEF - 3...이런식으로
# 조건2 ) 숫자들은 > 1  / 1, 0 은 없음.
# 조건3 ) 알파벳 길이는 2~15 이다.

code = input()
dial = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I'],
        ['J', 'K', 'L'], ['N', 'M', 'O'],
        ['P', 'Q', 'R', 'S'], ['T', 'U', 'V'], ['W', 'X', 'Y', 'Z']]
phoneNumber = ''
time = 0
for word in code:
    for num in dial:
        if word in num:
            time += dial.index(num) + 3
            phoneNumber += str(dial.index(num) + 2)

print(time)
print(phoneNumber)
