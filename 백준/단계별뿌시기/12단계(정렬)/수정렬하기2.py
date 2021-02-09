# https://www.acmicpc.net/problem/2751
# n = int(input())
# a = []
# for i in range(n):
#     a.append(int(input()))

# 정렬은 알고리즘방식도 있지만, sorted(), sort() 내장함수를 사용하는 방법을 알고 있자.

import sys
n = int(sys.stdin.readline())
b = []
for i in range(n):
    b.append(int(sys.stdin.readline()))
print(*b, sep='\n')
# 분할 정복 방식 - 병합정렬
