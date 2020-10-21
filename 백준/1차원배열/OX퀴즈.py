# 백준 8958번
# OOXXOXXOOO 같이 문제의 결과가 있다.
# 연속되는 0의 등장하면 점수를 연속된 0의 수만큼 계산
# input>>
# 5
# OOXXOXXOOO
# OOXXOOXXOO
# OXOXOXOXOXOXOX
# OOOOOOOOOO
# OOOOXOOOOXOOOOX
# output >>
# 10
# 9
# 7
# 55
# 30
n = int(input())
a = []
for t in range(n):
    a.append(str(input()))
for i in range(n):
    quiz = list(a[i])
    count = 0
    result = []
    un = 0
    for j in quiz:
        if j == 'X':
            un = 1
            count = 0
        elif j == 'O':
            un = 0
            if un == 0:
                count += 1
                result.append(count)
    print(sum(result))
