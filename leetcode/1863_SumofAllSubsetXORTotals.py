# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
# 주어진 리스트의 각 요소의 조합의 xor연산을 하였을때,
# 각 값의 합을 구하여라
from typing import List


class Solution:

    def use_iter(self, nums: List[int]) -> int:

        result, subset = 0, [0]

        for n in nums:
            new_subset = subset[:]

            # 조합에 대한 xor연산을 한다.
            for i in subset:
                print('subset:', subset)
                new_subset.append(n ^ i)
                print('n ^ i: ', n, i)
                # result += new_subset[-1]

            subset = new_subset

        # result를 리턴해도 되지만, new_subset의 합을 리턴해도 되더라구요.
        print('new_subset:', new_subset)
        return sum(new_subset)

    def use_recursion(self, nums: List[int]) -> int:

        # 재귀에 활용할 함수 정의
        def sums(term, idx):

            # 재귀가 멈추는 조건
            if idx == len(nums):
                print(term)
                return term

            # 각 요소의 조합에 맞춰 xor연산을 진행한다.
            return sums(term, idx+1) + sums(term ^ nums[idx], idx + 1)

        return sums(0, 0)

    def use_bit(self, nums: List[int]) -> int:
        result = 0
        load = []

        # 리스트의 길이를 비트 연산을 적용하면, 조합의 갯수가 된다.
        # list길이가 2이면, 조합의 종류는 4가지
        # 길이가 3이면, 조합의 종류는 8가지
        # 길이가 4이면, 조합의 종류는 16가지가 된다. 다 2에 길이승을 하면 조합의 갯수
        for n in range(1 << len(nums)):
            term = 0

            for i in range(len(nums)):

                if n & 1:
                    term ^= nums[i]

                n >>= 1

            result += term
            load.append(term)

        print('모든 조합의 xor합 종류 :', load)
        return result


ex = [1, 3]
sol = Solution()
print('===========리스트를 활용한 방법==========')
print(sol.use_iter(ex))
print('=========재귀를 활용한 방법============')
print(sol.use_recursion(ex))
print('=========비트연산자를 활용한 방법============')
print(sol.use_bit(ex))
