# https://app.codesignal.com/arcade/code-arcade/corner-of-0s-and-1s/6SLJChm9N3fEgr2R7
def equalPairBit(n, m):
    # print(bin(n), list(bin(n)))          # ['0', 'b', '1', '0', '1', '0']
    # print(bin(m), list(bin(m)))  # ['0', 'b', '1', '0', '1', '1']
    # print(list(reversed(list(bin(n)))))  # ['0', '1', '0', '1', 'b', '0']
    # print(list(reversed(list(bin(m)))))  # ['1', '1', '0', '1', 'b', '0']
    print(2 ** 4)
    print(2 ^ 7)
    print(bin(n)[-1], bin(n)[-2])
    print('xor', 10 ^ 11)
    print('not', ~10, ':', bin(~10))
    print('not', ~11, ':', bin(~11))
    return ~(n ^ m) & ((n ^ m)+1)
# 이진법으로 바꾸고, 보수와 XOR연산으로 바꾸어서, 계산한다. 가장 오른쪽에 같은 값이 나오는 자리 값(이진상태에서)


equalPairBit(10, 11)
