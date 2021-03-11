class Mammel(object):
    #정답구문
    def __init__(self, age):
        self.age = age
    def __str__(self):
        return '{} y.o. in human age'.format(self.toHuman())
    def toHuman(self):
        return self.age

class Cat(Mammel):
    def toHuman(self):
        if self.age == 0 :
            return 0
        elif self.age < 3:
            return 25 // (3 - self.age)
        else:
            return 25 + 4 * (self.age -2)

class Dog(Mammel):
    def toHuman(self):
        if self.age == 0:
            return 0
        elif self.age == 1:
            return 15
        elif self.age == 2:
            return 24
        else:
            return 24 + (self.age -2) * 4

class Human(Mammel):
    pass

def toHumanAge(members):
    #species라는 dict에서 class를 지정하여 해당 값이 불러지면, 
    #해당 클래스에 int(age)라는 파라미터가 들어가게 되고 그것은 자연스럽게
    #str 함수에 들어가고 리턴해준다. 
    species = {
        'cat' : Cat,
        'dog' : Dog,
        'human' : Human
    }
    res = []
    for spec, age in members:
        res.append(str(species[spec](int(age))))
    return res