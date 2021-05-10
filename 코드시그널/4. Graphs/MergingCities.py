def mergingCities(roads):
    i = 0
    print(*roads, sep='\n')
    while i + 1 < len(roads):
        if roads[i][i + 1]:
            print('now:', i, i+1)
            for j in range(len(roads[i + 1])):
                if roads[i + 1][j] and i != j:
                    # 병합하는 라인 City i +1에서 Ture값들을 다 City i 에 반영한다.
                    # 단, i == j 인 경우에는 반연하지 않아서 i = 0인 경우 0 번째 인자는
                    # 0 이유지 된다.
                    roads[i][j] = roads[j][i] = True
            print(roads[i])
            del roads[i + 1]
            print(f'******병합 del {i+1}***********')
            print(*roads, sep='\n')

            # 병합을 완료하였으면, 병합을 한 요소번째 인자들을 다 지워준다.
            for j in range(len(roads)):
                del roads[j][i + 1]

            print(f'=={i+1} del===========')
            print(*roads, sep='\n')
            # i의 움직임은 특이하다, 처음에는 0으로 시작해도 해당되는 노드들이 감소하기 때문에
            # -1을 하여 -1로 되었다가
            i -= 1
        # 반복이 끝나면 +2를 하여 0, 2, 4 식으로 움직이는 모션을 준다.
        i += 2
    return roads


roadRegister = [[False, True, True, False, False, False, True],
                [True, False, True, False, True, False, False],
                [True, True, False, True, False, False, True],
                [False, False, True, False, False, True, True],
                [False, True, False, False, False, False, False],
                [False, False, False, True, False, False, False],
                [True, False, True, True, False, False, False]]

print(mergingCities(roadRegister))

a, b = {1, 2}, {3, 4}
print(a | b)
