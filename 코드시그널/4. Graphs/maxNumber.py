from itertools import permutations as pm
a = [3,30,34,5,9,21,2,27]
b = [x//(10**(len(str(x))-1)) for x in a]
result = ''
while b :
    print('now b ==>',b)
    m = max(b)
    count = 0
    print('nowMAX = ',m,'count = ', count)
    for i in b : 
        if i == m :
            count +=1

    if count == 1:
        result += str(m)
        b.remove(m)
    elif count >1:
        c = enumerate(b)
        same_index = [i for i, value in c if value == m]
        
        same = [a[j] for j in same_index]
        print(same_index, same)
        result += max(list(''.join(map(str, i)) for i in list(pm(same, len(same)))))
        for n in range(count):
            b.remove(m)
        print('b = ', b)
    else:
        print('error')

print(result)