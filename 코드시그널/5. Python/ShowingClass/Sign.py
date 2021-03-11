class Functions(object):
    @staticmethod
    def sign(x):
        if x>0: return 1
        elif x<0: return -1
        else: return 0

def sign(x):
    return Functions.sign(x)

sample = -34
print(sign(sample))

# 원해 sign에 원하는 조건을 추가하기 위해서 위의 staticmethod를 통해서 조건을 달아주었다. 
# 이렇게 한뒤 sign에 return값을 위의 staticmethod아래의 같은 이름의 Sign을 해주면된다. 
# staticmethod는 따로 self를 안써도 되고 그냥 바로 쓰면된다. 