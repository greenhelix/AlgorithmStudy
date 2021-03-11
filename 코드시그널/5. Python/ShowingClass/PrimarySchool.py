class Rectangle(object):
    def __init__(self, height, width):
        self.height = height
        self.width = width
    
    def __str__(self):
        return '{} x {} = {}'.format(self.height, self.width, self.area)
    
    #이부분이 문제 여기서 area를 어떻게 만들어서 넣을 것인가.
    @property
    def area(self):
        return self.height * self.width
    

def primarySchool(height, width):
    return str(Rectangle(height, width))

sh = 7
sw = 4
print(primarySchool(sh, sw))

# 이 문제는 주어진 Rectangle 클래스에서 이미 init, str이 설정되엉 있다. 그런데, area는 어디에도 
# 선언이 안되어 있고 area는 height와 width를 곱한 넓이 값이 되야 한다. 
# 이러한 경우 proerty를 통해 값을 설정해주고 class의 자원으로 활용하면된다. 
# @property는 getter 의 개념이고, @area.setter는 setter의 개념이다. 
# 잘 활용하면 좋다.