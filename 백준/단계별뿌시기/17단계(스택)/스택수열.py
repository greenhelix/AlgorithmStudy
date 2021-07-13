# 1~n 스택 넣었다가, 뽑아서 하나의 수열 만든다.
# push는 반드시 오름차순으로 넣어진다.
# 1<=n <=100,000 범위
# n개의 줄 수열 1~n 이하 정수가 입력 된다.
# 출력: push 는 +  pop 은 - 으로 표현한다, 불가능은 NO 로 출력 한다.

n = int(input())
stack, result = [], []
count, msg = 1, 1

for i in range(n):
    x = int(input())

    while count <= x:
        stack.append(count)
        result.append("+")
        count += 1

    if stack[-1] == x:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        msg = 0
        break

if msg:
    print("\n".join(result))


# 8
# 4
# 3
# 6
# 8
# 7
# 5
# 2
# 1
