# https://leetcode.com/problems/count-of-matches-in-tournament/

# 팀의 갯 수 : n , 각 짝수 n개의 팀은 경기의 수가 n/2이다.
# 홀수 n개의 팀인 경우는 n/2+1 의 경기가 진행된다. 최종 우승자 1명이 될때까지 경기의 총 횟수를 출력해주는 함수를 만들어라.

class Solution:

    def use_recursion(self, n: int) -> int:

        self.matches = 0

        def check_match(n: int):

            if n == 1:
                return
            elif n % 2 == 0:
                self.matches += n // 2
                check_match(n//2)
            elif n % 2 >= 1:
                self.matches += n // 2
                check_match(n // 2 + 1)

        check_match(n)

        return self.matches


n = 7
sol = Solution()
print(sol.use_recursion(n))
