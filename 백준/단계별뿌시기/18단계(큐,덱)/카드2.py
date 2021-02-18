# https://www.acmicpc.net/problem/2164
from collections import deque
n = int(input())
# cards = deque(i for i in range(1, n+1))
# print('cards = ', cards)
# def job(card: deque):
#     card.popleft()
#     print('1번작업 후 카드상태:', card)
#     if len(card) == 1:
#         print('한장남았습니다.')
#         result = card[0]
#         return result
#     temp = card.popleft()
#     card.append(temp)
#     print('2번작업후 카드 상태:', card)
# while len(cards) > 1:
#     result = job(cards)
# print(result)

cards = deque(i for i in range(1, n + 1))
print(cards)
# while not(len(cards)==1): same meaning, Increase Intuition method
while len(cards) > 1:
    cards.popleft()
    temp = cards.popleft()
    cards.append(temp)

print(cards[0])
