# https://www.acmicpc.net/problem/1541

# -을 기준으로 찢어서 저장해준다.
a = input().split('-')
print(a)  # ['55', '50+40']
show = []
for i in a:
    cnt = 0
    s = i.split('+')
    print('s::', s)
    for j in s:
        cnt += int(j)
    show.append(cnt)
n = show[0]
print(show)
for i in range(1, len(show)):
    n -= show[i]

print(n)
