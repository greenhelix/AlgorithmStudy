# https://leetcode.com/problems/zigzag-conversion/
test = 'PAYPALISHIRING'
row = 4

def convert(s : str, r : int) -> str:
    bucket = dict()
    pointer, down, up, move = 0, 1, -1, 0
    
    for c in s : 
        
        # 이동 범위를 설정하고, 범위 내에서 다시 올라갈 수 있도록 조건을 짠다.
        if pointer == 0: 
            move = down
        elif pointer == r - 1:
            move = up
        
        # 딕셔너리에 해당 포인터위치로 문자열을 합치는 형식으로 딕셔너리에 넣어준다.
        bucket[pointer] = bucket.get(pointer, '') + c
        # 포인터를 move 를 추가해서 방향성을 잡아준다.
        pointer += move
    
    print(bucket) 
    # 0: 'PIN', 1: 'ALSIG', 2: 'YAHR', 3: 'PI'}
    
    # 최종 join 함수를 통해서 합쳐준다. 
    return ''.join(bucket.values())
    

print(convert(test, row))