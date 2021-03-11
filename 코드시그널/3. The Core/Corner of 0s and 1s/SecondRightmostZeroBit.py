
def secondRightmostZeroBit(n):
    print(bin(n)[2:])
    print(bin(8))
    print(bin(8)[:1:-1])
    # 0을 계속 끄집어내느 함수이지만, 그 리스트에서 2번째 값을 가져오면 2번째 0의 위치가 된다.
    return 2**(list(index for index, value in enumerate(bin(n)[:1:-1]) if value== '0'))[1]

print(secondRightmostZeroBit(37))
print()
print(secondRightmostZeroBit(4))