# n, m = map(int, input().split())
# number = [i + 1 for i in range(n)]
# checker = [False] * n
# result = []


# def dfs(s):
#     print('현재 s= ', s)
#     if s == m:
#         print('result출력!')
#         print(*result)
#         return
#     for i in range(n):
#         if checker[i]:
#             print('checker', i, '가 True여서 계속진행.')
#             continue
#         print(number[i], '를 result에 넣어줍니다.')
#         result.append(number[i])

#         dfs(s + 1)
#         checker[i] = True
#         result.pop()
#         print('now i ', i)
#         for j in range(i + 1, n):
#             checker[j] = False
#         print('반복문 후 Checker False넣기', checker)


# dfs(0)
