# https://www.acmicpc.net/problem/2675

# 첫번째 입력값 = 테스트케이스 수
# 두번째 입력값 = 반복횟수 R
# 세번째 입력값(띄어쓰기로 입력) = 해당 문자 S
# 2
# 3 ABC
# 5 /HTP
# AAABBBCCC
# /////HHHHHTTTTTPPPPP

N = int(input())  # 테스트케이스 갯수
for t in range(N):
    R, S = input().split()  # 반복횟수, 문자값
    result = ''
    for i in range(len(S)):
        result += S[i] * int(R)
    print(result)

# 문자값 길이 만큼 각 문자를 반복횟수만큼 result안에 추가해서 붙여준다.
