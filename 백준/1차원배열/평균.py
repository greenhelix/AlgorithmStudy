# 백준 1546번
# 점수중에 최댓값M
# 모든 점수를 점수/M*100
# 이렇게 모든 점수값을 변화 준뒤, 평균을 구한다.
# input>> 3 \n 40 80 60
# output >> 75.0
n = int(input())
a = list(map(int, input().split()))
b = max(a)
for i in range(n):
    a[i] = a[i]/b * 100

print(sum(a)/n)
