# https://www.acmicpc.net/problem/4673

# 문제: 셀프 넘버 (ex: d(75) = 75 + 7+ 5 = 87) 개념이 있는데,
# 여기서 75는 87의 생성자라고 한다.
# 100이 넘어가면 생성자가 한개이상인 경우가 생김.(91, 100)
# 이렇게, 생성자가 없는 숫자를 셀프 넘버라고 한다.
# 10000보다 작거나 같은 셀프 넘버를 한 줄에 하나씩 출력하세요.

# 생성자를 만드는 조건은 자기 자신과 각 자릿수의 합을 했을때이다.
# 1, 3, 5, 7, 9, 20, 31, 42, 53, 64, 75, 86, 97 은 그러한 생성자 계산으로
# 구할 수가 없는 숫자들이다.
# 입력은 없고, 출력만 한다.

# 짝수가 포함안되는 이유, 홀수들은 한자릿수에서, 자기 자신과, 자기 자신을 더했을
# 때, 무조건 짝수가 된다. 그래서 빠진다. 그리고 짝수들은 생성자가 무조건 존재한다.

# a = "123"
# print(int(a) % 10)
# print(int(a[:-1]) % 10)
# print(int(a[:-2]) % 10)
# print(int(a) % 10)
# print(int(a[1]))
# print(int(a[2]))

# N = int(a) % 10 + int(a) #1
# N = (int(a) + int(a[0])) % 10 + int(a) #10
# N = (int(a) + int(a[0]) + int(a[1])) % 10 + int(a) #100
# N = (int(a) + int(a[0]) + int(a[1])+int(a[2])) % 10 + int(a) #1000
# N = (int(a) + int(a[0]) + int(a[1])+int(a[2])+int(a[3])) % 10 + int(a) #10000
# def selfNum():
#     num = [i for i in range(1, 101)]
#     num2 = [i for i in range(1, 101)]
#     for a in num:
#         N = a + sum(list(map(int, str(a))))
#         if N in num:
#             num2.remove(N)
#     for e in num2:
#         print(e)


# selfNum()

A = set(range(1, 101))
B = set()
for i in range(1, 101):
    for j in str(i):
        i += int(j)
    B.add(i)
re = A - B

print(*sorted(re), sep="\n")
