# https://www.acmicpc.net/problem/11720
# N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

N = int(input())
print(sum(map(int, list(input()))))
# result = 0
# for i in range(N):
#     result += int(num[i])
# print(result)
