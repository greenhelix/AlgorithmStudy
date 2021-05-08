# 신규 게임 ‘카카오 미로 탈출’이 출시되어, 라이언이 베타테스터로 참가했습니다.

# Maze.png

# 위 예시 그림은 카카오 미로 탈출의 초기 상태를 나타냅니다. 1번부터 3번까지 번호가 붙어있는 3개의 방이 있고, 방과 방 사이를 연결하는 길에는 이동하는데 걸리는 시간이 표시되어 있습니다. 길은 화살표가 가리키는 방향으로만 이동할 수 있습니다. 미로에는 함정이 존재하며, 함정에 걸리면 함정과 연결된 모든 화살표의 방향이 바뀝니다.
# 출발지점인 1번 방에서 탈출이 가능한 3번 방까지 이동해야 합니다. 탈출하는데 걸리는 최소 시간을 구하려고 합니다.

# 그림의 원은 방을 나타내며 원 안의 숫자는 방 번호를 나타냅니다.
# 방이 n개일 때, 방 번호는 1부터 n까지 사용됩니다.
# 화살표에 표시된 숫자는 방과 방 사이를 이동할 때 걸리는 시간을 나타냅니다.
# 화살표가 가리키고 있는 방향으로만 이동이 가능합니다. 즉, 위 그림에서 2번 방에서 1번 방으로는 이동할 수 없습니다.
# 그림에 표시된 빨간색 방인 2번 방은 함정입니다.
# 함정 방으로 이동하는 순간, 이동한 함정 방과 연결되어있는 모든 길의 방향이 반대가 됩니다.
# 위 그림 1번 방에서 2번 방으로 이동하는 순간 1에서 2로 이동할 수 있던 길은 2에서 1로 이동할 수 있는 길로 바뀌고, 3에서 2로 이동할 수 있던 길은 2에서 3으로 이동할 수 있는 길로 바뀝니다.
# 똑같은 함정 방을 두 번째 방문하게 되면 원래 방향의 길로 돌아옵니다. 즉, 여러 번 방문하여 계속 길의 방향을 반대로 뒤집을 수 있습니다.
# 미로를 탈출하는데 필요한 최단 시간은 다음과 같습니다.
# 1→2: 2번 방으로 이동합니다. 이동 시간은 2입니다.
# 함정 발동: 2번 방과 연결된 모든 길의 방향이 반대가 됩니다.
# 2→3: 3번 방으로 이동합니다. 이동 시간은 3입니다.
# 탈출에 성공했습니다. 총 이동시간은 5입니다.
# 방의 개수를 나타내는 정수 n, 출발 방의 번호 start, 도착 방의 번호 end, 통로와 이동시간을 나타내는 2차원 정수 배열 roads, 함정 방의 번호를 담은 정수 배열 traps이 매개변수로 주어질 때, 미로를 탈출하는데 필요한 최단 시간을 return 하도록 solution 함수를 완성해주세요.
n = 3
start = 1
end = 3
roads = [[1, 2, 2], [3, 2, 3]]
traps = [2]


def solution(n, start, end, roads, traps):
    answer = 0
    pos = start

    while pos != end:
        for info in roads:
            if info[0] == pos:
                # print('go!', info)
                next = info[1]
                pos = next
                answer += info[2]
                if pos in traps:
                    # print('trap!!', pos ,'reverse')
                    for r in roads:
                        if r[0] == pos or r[1] == pos:
                            r[0], r[1] = r[1], r[0]

                    # print(roads)
            if pos == end:
                # print('end!')
                break
    return answer
