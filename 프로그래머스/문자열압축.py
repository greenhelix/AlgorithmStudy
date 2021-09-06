text = "aabbaccc"
text2 = "abababcdcdababcdcdcd"
text3 = "abcabcabc"

# 시간 복잡도 O(n^2)
# 반복문을 이중으로 사용하였기 때문에 최악의 경우 n제곱의 시간이 든다.


def study(s):
    check = []
    temp = ""

    if len(s) == 1:
        return 1

    for i in range(len(s) // 2 + 1, 0, -1):
        case = s[:i]
        cnt = 1
        for j in range(i, len(s), i):
            if s[j: j + i] == case:
                cnt += 1
            else:
                if cnt == 1:
                    cnt = ""
                temp += str(cnt) + case
                case = s[j: j + i]
                cnt = 1

        if cnt == 1:
            cnt = ""
        temp += str(cnt) + case
        check.append(len(temp))
        temp = ""

    return min(check)


# print(study(text3))


def prac(s):
    길이집합 = []
    압축단어 = ""

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        압축단위 = s[:i]
        압축횟수 = 1

        for j in range(i, len(s), i):

            # 내부에서 글자단위로 압축을 진행하는 부분
            if 압축단위 == s[j: j + i]:
                압축횟수 += 1

            else:
                if 압축횟수 == 1:
                    압축횟수 = ""
                압축단어 += str(압축횟수) + 압축단위
                압축단위, 압축횟수 = s[j: j + i], 1

        # 단위별 완료 된 경우 최종 압축단어를 만들어서 최종 길이를 측정하여 집합에 추가
        if 압축횟수 == 1:
            압축횟수 = ""
        압축단어 += str(압축횟수) + 압축단위
        길이집합.append(len(압축단어))
        압축단어 = ""

    print(길이집합)
    return min(길이집합)


print(prac(text3))
