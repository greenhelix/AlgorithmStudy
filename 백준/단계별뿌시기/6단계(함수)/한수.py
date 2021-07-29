# https://www.acmicpc.net/problem/1065

# 문제 :어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
# 주어진 입력값 N 이하의 수에서 한수의 갯수를 구하라.
# 첫째줄에1, 000보다작거나같은자연수N이주어진다.
# 첫째 줄에 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력한다.

# 등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다.
# N = int(input())


# def sequence(n: int):
#     count = 0
#     seq = []
#     for i in range(1, N+1):
#         t = str(i)
#         if len(t) == 1:
#             print(t, ':: 한자리')
#             count += 1
#         else:
#             for j in range(len(t) - 1):
#                 seq += [int(t[j + 1]) - int(t[j])]
#             print('시퀀스', t, '::', seq)

#         if len(seq) == 1:
#             print(t, '= 두자리')
#             count += 1
#             seq = []
#         elif len(seq) >= 2:
#             print(count)
#             for b in range(len(seq) - 1):
#                 if seq[b] == seq[b + 1]:
#                     print(t, '::sequence::')
#                 elif seq[b] != seq[b + 1]:
#                     print('no sequence out')
#                     seq = []
#                     break
#                 count += 1
#                 seq = []

#     return count


# print(sequence(N))

N = int(input())


def sequence(n: int):
    count = 0
    seq = []
    for i in range(1, N+1):
        t = str(i)
        if len(t) == 1:
            count += 1
        else:
            for j in range(len(t) - 1):
                seq += [int(t[j + 1]) - int(t[j])]
        if len(seq) == 1:
            count += 1
            seq = []
        elif len(seq) >= 2:
            for b in range(len(seq) - 1):
                if seq[b] != seq[b + 1]:
                    seq = []
                    break
                count += 1
                seq = []
    return count


print(sequence(N))
