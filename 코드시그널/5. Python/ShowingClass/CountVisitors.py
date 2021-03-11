class Counter(object):
    def __init__(self, value):
        self.value = value
    
    def inc(self):
        self.value += 1

    def get(self):
        return self.value

def countVisitors(beta, k, visitors):
    counter = Counter(beta)
    for visitor in visitors :
        if visitor >= k :
            counter.inc()
    return counter.get()

b = 22
k = 5
v = [4,6,6,5,2,2,5]

print(countVisitors(b,k,v))

# 가장 기본으로 주어진 Counter의 클래스를 정의하고 사용하려면, __init__이 필요하다. 
# 최초 init 의 정의는 위ㅇ와 같이 해주고, 들어오는 파라미터의 종류가 여러개면 여러개 받아주고, Self.변수명 = 변수명 으로 지정하고 생성
# 해주는 부분이라고 보면된다. 
