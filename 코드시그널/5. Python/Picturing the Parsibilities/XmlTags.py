import xml.etree.ElementTree as ET
from functools import reduce
def xmlTags(xml):
    root = ET.fromstring(xml)
    print('root = ',root) #<Element 'data' at 0x0000022A61EF19F8>
    result, q = [], []
    depth = "--"
    q.append((0, root))

    print(q) #[(0, <Element 'data' at 0x0000022A61EF19F8>)]
    while len(q)>0:
        (d, n) = q.pop()
        print('d= ',d) #0
        print('n= ',n) #<Element 'data' at 0x0000022A61EF19F8>
        for i in reversed(n):
            q.append((d+1, i))
        
        a = sorted(set(reduce(lambda b, e : b+e.keys(), root.findall(".//"+n.tag),[])))
        if d == 0:
            a = sorted(n.keys())
        
        s = "%s%s(%s)"%(depth * d , n.tag, ', '.join(a))
        print('a >>>',a)
        print('s >>>',s)

        if not s in result:
            result.append(s)
    
    return result

sample = "<data><animal name=\"cat\"><genus>Felis</genus><family name=\"Felidae\" subfamily=\"Felinae\"/><similar name=\"tiger\" size=\"bigger\"/></animal><animal name=\"dog\"><family name=\"Canidae\" member=\"canid\"/><order>Carnivora</order><similar name=\"fox\" size=\"similar\"/></animal></data>"
print(xmlTags(sample))