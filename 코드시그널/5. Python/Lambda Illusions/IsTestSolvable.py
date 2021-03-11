def isTestSolvable(ids, k):
    def digitSum(x): return sum(list(map(int, list(str(x)))))
    # digitSum = lambda x : sum(list(map(int, list(str(x)))))
    sm = 0
    for questionId in ids:
        sm += digitSum(questionId)
    return sm % k == 0


sample = [529665, 909767, 644200]
k = 3

print(isTestSolvable(sample, k))
# ids의 값들을 다 쪼개서 더한다.
# (5 + 2 + 9 + 6 + 6 + 5) + (9 + 0 + 9 + 7 + 6 + 7) + (6 + 4 + 4 + 2 + 0 + 0) = 87
# 87을 k로 나눠지면 True 아니면 False
