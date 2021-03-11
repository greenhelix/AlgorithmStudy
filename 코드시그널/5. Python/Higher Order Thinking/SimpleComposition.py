def compose (f, g):
    return lambda x : f(g(x))  #이 부분이 문제 부분이었다. 

def simpleComposition(f, g, x):
    return compose(eval(f), eval(g))(x)

sampleF = "math.log10"
sampleG = "abs"
sampleX = -100

print(simpleComposition(sampleF, sampleG, sampleX))

#이 문제는 문자열로 된, 수학식을 x를 eval적용을 두번해주는 방법을 보여준다. 
#lambda를 통해서 원하는 변수를 원하는 장소에 넣어주면된다. 
