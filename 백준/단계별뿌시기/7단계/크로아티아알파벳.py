# https://www.acmicpc.net/problem/2941
# 문자열
# 알파벳소문자, -, = 으로 이뤄진 문자열 IN -- 특정 조건의 크로아티아 알파벳 표기 참고하여 -- 사용된 크로아티아어 길이 OUT
# 조건1 ) 최대 100글자의 단어 입력
# 조건2 ) 표에 나온 것들 외에는 한 글자씩 센다.

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
for pick in croatia:
    word = word.replace(pick, '*')

print(word)
print(len(word))
# https://hongku.tistory.com/255
# replace를 통해서 해당 단어가 word에 있는지 확인해서 카운트에 용이한 단어로 바꾼다.
# 이렇게 되면, 마지막 길이를 재면 그냥 카운트 값이 나온다.
