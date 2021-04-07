# https://www.acmicpc.net/problem/11047
n, k = map(int, input().split())
coin = []
for _ in range(n):
    coin.append(int(input()))
check = 0

for i in range(n - 1, -1, -1):  # 제일 큰 값부터 시작해서 뒤로 움직인다. 0번째 인자까지
    if k == 0:  # 목표값이 0원이 되면, 반복을 끝낸다.
        break
    if coin[i] > k:  # 만약 동전이 k값보다 크다면 넘어간다.
        continue
    check += k // coin[i]  # 목표k값이 동전으로 나눠지면, 그 몫을 check에 담아둔다.
    k %= coin[i]  # 해당 목표값은 k를 최신화 시켜서 넘긴다.
    print(i, coin[i], k, check)

print(check)
