def mirrorBits(a):
    return int(format(a,'b')[::-1], 2)
    # return int(bin(a)[2:][::-1],2)
# 67이 입력되면 이진법으로 바꾼뒤, reverse 시켜서 다시 십진법으로 만드는 것이다.
print(mirrorBits(67))