def sortCodesignalUsers(users):
    res = [CodeSignalUser(*user) for user in users]
    res.sort(reverse = True)
    return list(map(str, res))

class CodeSignalUser(object):
    #들어오는 값은 리스트 이므로 원하느 방식으로 이렇게 잘라서 해도 되고, 
    # *args로 정의하고 self.name = args[0]...이런식으로 쭈욱 인덱스로 받아도 된다. 
    def __init__(self, username, id, xp):
        self.name = username
        self.id = int(id)
        self.xp = int(xp)
    # map(str,..)이 부분에서 사용되는 것이다. map에는 단순히 res의 name값만 사용한다는 것.
    def __str__(self):
        return self.name
    
    def __lt__(self, value):
        return (self.xp, value.id) < (value.xp, self.id)
        #xp는 내림차순, id는 오름차순이라 서로 위치가 다르다.
        #기본은 Self<value이니깐 이것이 내림, value<self 로 하면 오름차순이 된다.

samples = [["warrior","1","1050"], ["Ninja", "21", "995"], ["recruit","3","995"]]
print(sortCodesignalUsers(samples))
        