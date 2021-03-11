def twoTeams(students):
    return sum(students[0::2]) - sum(students[1::2])
# 짝수번 요소들의 합, 홀수번 요소들의 합을 뺀다.


sample = [1, 11, 13, 6, 14]
print(twoTeams(sample))
