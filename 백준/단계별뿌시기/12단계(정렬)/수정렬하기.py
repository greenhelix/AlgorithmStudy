# https://www.acmicpc.net/problem/2750
import time
start = time.time()
# n = int(input())
# a = set()
# for i in range(n):
#     a.add(int(input()))
# print(*a, sep='\n')

# set 말고, 단순히 내장함수를 사용한다 sorted, sort
n = int(input())
b = []
for i in range(n):
    b.append(int(input()))

print(*sorted(b), sep='\n')
print(time.time() - start)
