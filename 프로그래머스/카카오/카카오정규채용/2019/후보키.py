from itertools import combinations as comb


def solution(table):
    answer = []

    # 조합 생성(컬럼의 인덱스로 구성된 조합)
    행, 열 = len(table), len(table[0])
    조합 = []
    for i in range(1, 열 + 1):

        조합.extend(comb(range(열), i))

    # 유일성 체크
    유일성 = []
    for kind in 조합:

        # 실제 데이터를 조합에 맞춰 넣어본다.
        temp = [tuple([item[i] for i in kind]) for item in table]

        # 실제 데이터를 넣은 조합의 길이가 set으로 중복제거를 했을때,
        # 행의 길이와 일치하면 유일성이 성립한다.
        if len(set(temp)) == 행:
            유일성.append(kind)  # 유일성을 성립하는 인덱스 조합을 넣어준다.

    # 최소성 체크
    최소성 = set(유일성)  # 유일성 list를 set으로 형변환 discard를 사용하기 위함.
    # print(유일성)
    for i in range(len(유일성)):

        for j in range(i + 1, len(유일성)):

            # & set 의 교집합 관계를 사용하여
            # i, j의 교집합이 i의와 같다면 슈퍼키가 포함되어있는 것이므로
            # j요소를 버려준다.(remove로하면 에러발생)
            if list(유일성[i]) == list(set(유일성[i]) & set(유일성[j])):
                # print(
                #     f'{유일성[i]}&{유일성[j]} => {list(set(유일성[i]) & set(유일성[j]))}:::{유일성[j]}버림')
                최소성.discard(유일성[j])
            # else:
            #     print(f'무시한다.{유일성[j]} PASS')

        # print(최소성, '\n')

    # print(최소성)

    return len(최소성)


db = [["100", "ryan", "music", "2"],
      ["200", "apeach", "math", "2"],
      ["300", "tube", "computer", "3"],
      ["400", "con", "computer", "4"],
      ["500", "muzi", "music", "3"],
      ["600", "apeach", "music", "2"]]

print(solution(db))
