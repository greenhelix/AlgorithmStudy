# [10818번 최소, 최대](https://www.acmicpc.net/problem/10818)
a = int(input())
b = list(map(int, input().split()))
print(min(b), max(b))

# [2562번 최댓값](https://www.acmicpc.net/problem/10818)
a = [int(input()) for i in range(9)]
print(max(a))
print(a.index(max(a))+1)

# [2577번 숫자의 개수](https://www.acmicpc.net/problem/2577)
a = int(input())
b = int(input())
c = int(input())
d = str(a * b * c)
count = [0] * 10
for i in range(10):
    for j in range(len(d)):
        if i == int(d[j]):
            count[i] += 1
    print(count[i])

# [3052번 나머지](https://www.acmicpc.net/problem/3052)
b = set(int(input()) % 42 for i in range(10))
print('b = ', b, len(b))

# [1546번 평균](https://www.acmicpc.net/problem/1546)
n = int(input())
a = list(map(int, input().split()))
b = max(a)
for i in range(n):
    a[i] = a[i]/b * 100
print(sum(a)/n)

# [8958번 OX퀴즈](https://www.acmicpc.net/problem/8958)
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

# [4344번 평균은 넘겠지](https://www.acmicpc.net/problem/4344)
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
