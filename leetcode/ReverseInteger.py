# https://leetcode.com/problems/reverse-integer/
a , b ,c= 123, -123, 1534236469
def reverseInteger(x : int) -> int: 
    result = list()
    minusPlus = list()
    for i in str(x):
        if i == '-':
            minusPlus.append(i)
        else:
            result.append(i)
    
    result = minusPlus + list(reversed(result))
    print('show:', result)
    result = int(''.join(result))
    # if result > float('inf') and result < float('-inf'):
    if result >= 2** 31 -1 or result <= -2** 31:
        return int(''.join(result))
    else: 
        return 0
    
print(reverseInteger(c))