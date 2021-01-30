# https://www.acmicpc.net/problem/9461
# P(N) 파도반 수열 - 정삼각형의 나선 P(1)~ P(10) 1,1,1,2,2,3,4,5,7,9
# i = 1 P(i) + P(i+1) = P(i+3)
# 1<= N <= 100
t = int(input())
p = [0 for i in range(101)]
print(p)
p[1], p[2], p[3] = 1, 1, 1
for i in range(0, 98):
    p[i + 3] = p[i] + p[i + 1]

for i in range(t):
    n = int(input())
    print(p[n])
