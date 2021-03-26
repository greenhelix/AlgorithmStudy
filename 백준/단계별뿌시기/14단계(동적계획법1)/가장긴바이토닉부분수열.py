# https://www.acmicpc.net/problem/11054
# 수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열
# ex) {10, 20, 30, 25, 20}
n = int(input())
s = list(map(int, input().split()))
dpleft, dpright = [0] * n, [0]*n
print(n, s)
print(dpleft, dpright)
dpleft[0], dpright[0] = 1, 1


for i in range(1, n):
    l, r = 0, 0
    for j in range(i):
        if s[i] > s[j]:
            l = max(dpleft[j], l)
    for j in range(n-i, n):
        if s[n - i] > s[j]:
            r = max(dpright[j], r)
    dpleft[i] = l + 1
    dpright[n - i] = r + 1
print(dpleft, dpright)

print(max(list(map(lambda x, y: x+y, dpleft, dpright)))-1)
