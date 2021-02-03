# https://www.acmicpc.net/problem/11729
# 재귀
def hanoi(n, a, b, c):
    if n == 1:
        move.append([a, c])
    else:
        hanoi(n - 1, a, c, b)
        move.append([a, c])
        hanoi(n - 1, b, a, c)


move = []
hanoi(int(input()), 1, 2, 3)
print(len(move))
print(move)
print('\n'.join([' '.join(str(i) for i in row) for row in move]))
# https://m.blog.naver.com/PostView.nhn?blogId=mathplant00&logNo=220489897756&proxyReferer=https:%2F%2Fwww.google.com%2F
# https://ko.wikipedia.org/wiki/%ED%95%98%EB%85%B8%EC%9D%B4%EC%9D%98_%ED%83%91
# https://ko.khanacademy.org/computing/computer-science/algorithms/towers-of-hanoi/a/towers-of-hanoi
