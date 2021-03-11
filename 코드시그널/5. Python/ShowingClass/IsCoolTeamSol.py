
class Team(object):
    def __init__(self, names):
        self.names = names
    
    def __bool__(self):
        from collections import Counter, defaultdict as ddict
        IN, OUT = Counter(), Counter()
        g = ddict(set)
        for name in self.names:
            #i 와 j에 각 단어의 첫글자와 끝글자를 넣는다.
            i, j = name[0].lower(), name[-1].lower()
            #g
            g[i].add(j)
            g[j].add(i)

            IN[j] +=1
            OUT[i] +=1
        print(g)
        print(IN)
        print(OUT)
        # d = [IN[x]-OUT[x] for x in IN+OUT if IN[x] != OUT[x]]
        d = []
        for x in IN+OUT :
            print(x)
            if IN[x] != OUT[x]:
                d.append(IN[x]-OUT[x])
                print(d)
        print(IN+OUT)
        print(d)
        s ={i}
        path = [i]
        print('최초 ', s, path)
        print(g)
        while path :
            print(path)
            node = path.pop()
            print(node,'node')
            for i in g[node]:
                if i not in s:
                    s.add(i)
                    path.append(i)
        print(s)
        return (not d or d[0] * d[1] == -1) and len(s) == len(g)

def isCoolTeam(team):
    return bool(Team(team))

test = ['Mark','Kelly','Kurt','Terk']
team = ['Sopie','Boris',"Eric",'Charlotte']
fail = ['Rob','Bobby','Billy']
print(isCoolTeam(fail))