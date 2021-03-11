def removeTasks(k, toDo):
    del toDo[k - 1::k]
    return toDo


sample = [1237, 2847, 27485, 2947, 1, 247, 374827, 22]
s = 3
print(removeTasks(s, sample))
# k번째 요소를 제거하고 그 다음 k번째 요소도 제거 반복함.
# k배수의 요소들을 한 문장 del()을 사용해서 제거하라
