# 닉네임 변경 방법
# 1. 나간후, 새로운 닉네임 가능
# 2. 채팅방에서 닉네임 변경
# 입장시 출력문/ 퇴장시 출력문
# 중복닉네임 허용, 닉네임 변경시 출력문 닉네임도 변경
# record를 보고 최종적으로 출력될 배열을 리턴
def solution(record):
    # enter 유저아이디 닉네임 형식으로 입장
    # leave 유저아이디 로 퇴장
    # change 유저아이디 닉네임 해당 닉네임으로 변경
    # 유저아이디, 닉네임 소/대문자 구분 길이, 1이상10이하
    log = []
    name = {}
    for i in range(len(record)):
        state = record[i].split()

        if state[0] == 'Enter':
            log.append((state[1], '님이 들어왔습니다.'))
            name[state[1]] = state[2]
        elif state[0] == 'Leave':
            log.append((state[1], '님이 나갔습니다.'))
        elif state[0] == 'Change':
            name[state[1]] = state[2]

    for index, ele in enumerate(log):
        if ele[0] in name:
            nick = name[ele[0]]
            log[index] = (nick, ele[1])

    print(log)
    answer = [''.join(l) for l in log]
    return answer


reco = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
        "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(*solution(reco), sep='\n')
