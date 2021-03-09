# https://www.acmicpc.net/problem/10814
n, people = int(input()), []
for _ in range(n):
    age, name = map(str, input().split())
    people.append([int(age), name])
for i in sorted(people, key=lambda i: [i[0]]):
    print(i[0], i[1])
