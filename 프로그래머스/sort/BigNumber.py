from itertools import permutations as pm


def solution(numbers):
    return max(list(''.join(map(str, i)) for i in list(pm(numbers, len(numbers)))))


number1 = [3, 30, 34, 5, 9, 2, 21]
number2 = [6, 10, 2]


def solutions(a):
    result = ''
    b = [((x//(10**(len(str(x))-1))), y) for y, x in enumerate(a)]
    print('a= ', a, '\nb = ', b)

    for j in range(len(b)):

        print('now Max = ', max(b))
        count = 0

        # 중복 확인 검사
        for value, i in b:
            if max(b)[0] == value:
                count += 1

        print('max(b) =', max(b), 'count = ', count)
        print('if check start')

        if count == 1:
            print('append a of.. ', a[max(b)[1]])
            result += str(a[max(b)[1]])
            b.remove(max(b))
            print('now res = ', result)
        elif count > 1:

            m = max(b)[0]
            sam = []
            ans = ''
            for value, i in b:
                print(b)
                print('show! ', value, ',', i)
                if value == m:
                    print(a[i])
                    sam.append(a[i])
                    print('remove!')
                    b.remove((value, i))
            print(m, 'same thing = ', sam)
            sh = max(list(''.join(map(str, i))
                          for i in list(pm(sam, len(sam)))))
            print(sh, ' append!')
            result += sh
            print('now res = ', result)

        print(b)
    return result


solutions(number1)

number1 = [3, 30, 34, 5, 9]
number2 = [3, 30, 34, 5, 9, 2, 21]
number3 = [6, 10, 2]
solutions(number1)
# print(solution(number1))
# bb = [(0,3,9),(1,3),(2,3),(3,4),(4,5),(5,5),(6,9),(7,9),(8,9)]
