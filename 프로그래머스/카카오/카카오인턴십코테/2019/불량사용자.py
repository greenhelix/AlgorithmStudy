import re
from itertools import permutations as pm
from itertools import combinations as cb
sample = ["frodo", "fradi", "crodo", "abc123", "frodoc"]
test1, test2, test3 = set(), set(), set()
test4, test5, test6 = [], [], []

for i in sample:
    m = re.match('[\w]rodo', i)
    if m:

        test1.add(m.group())
        test4.append(m.group())
for i in sample:
    m = re.match('[\w]rodo', i)
    if m:

        test3.add(m.group())
        test5.append(m.group())
for i in sample:
    m = re.match('[\w][\w][\w][\w][\w][\w]', i)
    if m:

        test2.add(m.group())
        test6.append(m.group())

result = set()
