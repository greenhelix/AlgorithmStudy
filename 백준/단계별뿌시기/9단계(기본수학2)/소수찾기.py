# https://www.acmicpc.net/problem/1978
# n개의 소수중에서 소수가 몇개인지 찾아서 출력

# n은 100이하이다. 다음 n개의 수가 주어지는데 수는 1000이하의 자연수
n = int(input())
num = list(map(int, input().split()))
count = 0
if len(num) == n:
    for i in num:
        check = 0
        for j in range(1, i + 1):
            if i % j == 0:
                check += 1
        if check == 2:
            count += 1

print(count)
