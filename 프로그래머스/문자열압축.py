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

print(study(text3))
