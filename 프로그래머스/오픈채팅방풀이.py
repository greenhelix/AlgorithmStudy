def solution(record):
    answer = []
    name = {}
    # 로그찍히는 경우 정리
    state = {'Enter': '님이 들어왔습니다.',
             'Leave': '님이 나갔습니다.'}

    for i in record:
        ii = i.split(' ')   # 각 기록을 리스트화
        if ii[0] in ['Enter', 'Change']:    # 리스트의 첫 명령어 확인
            name[ii[1]] = ii[2]             # 닉네임 변경 명령어는 해당 uid의 닉네임을 변경

    print(name)

    for i in record:
        if i.split(' ')[0] != 'Change':     # Change빼고는 Answer에 추가해준다.
            answer.append(name[i.split(' ')[1]] +
                          state[i.split(' ')[0]])   # 문자열을 붙여주는 형태로 정답 리스트 형성
    return answer


reco = ["Enter uid1234 Muzi", "Enter uid4567 Prodo",
        "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]
print(*solution(reco), sep='\n')
