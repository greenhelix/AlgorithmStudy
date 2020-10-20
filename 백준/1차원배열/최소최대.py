# 백준 10818번
# 주어진 배열에서 최소값, 최대값을 출력
# 5
# 20 10 35 30 7
# >>> 7 35
a = int(input())
b = list(map(int, input().split()))
print(min(b), max(b))
