# https://www.acmicpc.net/problem/4949
# So when I die (the [first] I will see in (heaven) is a score list).
# [ first in ] ( first out ).
# Half Moon tonight (At least it is better than no Moon at all].
# A rope may form )( a trail in a maze.
# Help( I[m being held prisoner in a fortune cookie factory)].
# ([ (([( [ ] ) ( ) (( ))] )) ]).
#  .
# .
import re
s = ''
while 1:
    s = input()
    print(s)
    if s == '.':
        break
    ss = re.sub(r'[\w]', '', s)
    ss = ' '.join(ss).split()
    print(ss)

    check, isit = [], True

    for i in ss:
        if i == '(' or i == '[':
            check.append(i)
        elif i == ')':
            if not check or check[-1] == '[':
                isit = False
                print('break1')
                break
            elif check[-1] == '(':
                check.pop()
        elif i == ']':
            if not check or check[-1] == '(':
                isit = False
                print('break2')
                break
            elif check[-1] == '[':
                check.pop()
    if isit == True and not check:
        print('yes1')
    else:
        print('no')
