# https://www.acmicpc.net/problem/2798
# 세 장의 카드를 고르는 모든 경우를 고려하는 문제
# 브루트포스 알고리즘 (https://namu.wiki/w/%EB%B8%8C%EB%A3%A8%ED%8A%B8%20%ED%8F%AC%EC%8A%A4)
# 완전탐색


# 이 풀이로 풀면, 런타임 에러 발생
# from itertools import permutations, combinations
# n, m = map(int, input().split())
# card = list(combinations(list(map(int, input().split())), 3))
# results = []
# for i in card:
#     if sum(i) <= 500:
#         results.append(sum(i))
# print(max(results))
# 위의 풀이는 직접 브루트포스 알고리즘을 구현하지 않았기 때문에 틀렸다고 보는듯 하다.
# 브루트포스 알고리즘은 모든 경우의 수를 추출하여 주어진 조건에 맞는 값을 찾는 노가다 코드라고 볼 수 있다.

n, m = map(int, input().split())
card = list(map(int, input().split()))
result = 0
for i in range(n):
    for j in range(i + 1, n):
        for x in range(j + 1, n):
            if card[i] + card[j] + card[x] > m:
                continue
            else:
                result = max(result, card[i] + card[j] + card[x])
print(result)
