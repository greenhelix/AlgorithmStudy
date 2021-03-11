from collections import Counter 
team = ['Sopie','Boris',"Eric",'Charlotte']
test1 = ['Mark','Kelly','Kurt','Terk']
test2 = ['Rob','Bobby','Billy']
test3 = ['Caleb', 'Dale', 'Edward']
def check(name):
    head = list(name[i][0].lower() for i in range(len(name)))
    tail = list(name[i][-1].lower() for i in range(len(name)))
    print(head)
    print(tail)
    h = Counter(head)
    t = Counter(tail)
    print(h)
    print(t)
    ch = h & t
    print(ch)
    # dict(ch)
    # print(ch)
    print(sum(ch.values()))
    return True


check(team)
check(test1)
check(test2)
check(test3)