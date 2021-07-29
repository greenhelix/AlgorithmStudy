# https://www.acmicpc.net/problem/2908
# 구현
# 세자리수 두개 IN -- 거꾸로 읽는다  -- 거꾸로 봤을때 그 두 수 중 큰 수를 출력
# 조건 ) 두수는 세자리 수 이고, 0이 포함안되어 있다.
a, b = map(list, input().split())
a.reverse(), b.reverse()
print(a, b)
A = int(''.join(a))
B = int(''.join(b))
if A > B:
    print(str(A))
else:
    print(str(B))
