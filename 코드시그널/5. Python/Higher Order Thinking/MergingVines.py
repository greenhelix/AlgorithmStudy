def mergingVines(vines, n):
    def nTimes(n)  :
        def decorater(func):
            def wrapped(vines):
                for _ in range(n):
                    vines = func(vines)
                return vines
            return wrapped
        return decorater
#여기서 sumOnce는 파라미터가 한개만있었는데 이것을 반복하려고 하면, 
# 위의 mergingVines를 통해서 진행할 숭 ㅣㅆ다.
    @nTimes(n)
    def sumOnce(vines):
        res = [vines[i] + vines[i+1] for i in range(0, len(vines)-1, 2)]
        if len(vines) % 2 == 1:
            res.append(vines[-1])
        return res
    return sumOnce(vines)

testVine = [1,2,3,4,5]
n = 2

test2 = [1,2,3,4,5,6]
m = 10

print(mergingVines(testVine, n))
print(mergingVines(test2, m)) 
# print(sumOnce(test2,m)) 이런식으로는 안된다.

#이 문제는 주어진 sumonce의 함수를 추가적으로 수정하려고 한다. 그런데 
#이 수정부분이 큰 경우나 일일히 다 하기 힘든 경우 원하는 통일된 수정 포맷을 만들고
#그 아래에 원하는 함수들을 wrapped안에 불러들이면, 원하는 코드가 해당 코드에 덮여 쓰인상태로 
#가동된다.