# https://www.acmicpc.net/problem/2941

s1 = 'ljes=njak'
s2 = 'ddz=z='
s3 = 'nljj'

s = input()


def solution(s):

    croa = {'c=': '1', 'c-': '2', 'dz=': '3', 'd-': '4',
            'lj': '5', 'nj': '6', 's=': '7', 'z=': '8'}

    for k, v in croa.items():  # O(8)
        if k in s:
            s = s.replace(k, v)  # O(N)

    return len(s)


print(solution(s1))
print(solution(s2))
print(solution(s3))
