# https://www.acmicpc.net/problem/1181
n = int(input())
words = set()
for _ in range(n):
    w = input()
    c = len(w)
    words.add((c, w))

for i in sorted(words):
    print(i[1])
