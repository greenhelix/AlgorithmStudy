# https://www.acmicpc.net/problem/2751
import sys
n = int(sys.stdin.readline())
b = []
for i in range(n):
    b.append(int(sys.stdin.readline()))
print(*sorted(b), sep='\n')
