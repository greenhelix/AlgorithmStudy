class User(object):
    def __init__(self, username, _id, xp, name):
        self.username = username
        self._id = _id
        self.xp = xp
        self.name = name 
    #이 부분이 정답이다. 
    def __getattr__(self, attribute):
        return '{} attribute is not defined'.format(attribute)
    # 위의 속성들, username, id, xp , name외의 특성을 물어보는 경우, 해당 특성에 대한 멘트를 내보내준다. 
    # __getattr__는 init에서 없는 값이 들어오는 경우, 우선적으로 리턴해주는 함수라고 보면된다. 
def userAttribute(attribute):
    user = User("annymaster", '1234567', '1500', 'anny')
    return getattr(user, attribute)     

s1 = "_id"
s2 = "age"
print(userAttribute(s1))
print(userAttribute(s2))

