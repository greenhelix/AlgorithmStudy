# https://leetcode.com/problems/sum-of-all-subset-xor-totals/
from typing import List


class Solution:

    def subsetXORSum(self, nums: List[int]) -> int:
        result, subset = 0, [0]

        for n in nums:
            new_subset = subset[:]
            for i in subset:
                new_subset.append(n ^ i)
                result += new_subset[-1]

            subset = new_subset
        return result

    def subsetXORSum_recursion(self, nums: List[int]) -> int:
        def sums(term, idx):
            if idx == len(nums):
                return term
            return sums(term, idx + 1) + sums(term ^ nums[idx], idx + 1)
        return sums(0, 0)

    def subsetXORSum_bit(self, nums: List[int]) -> int:
        result = 0

        # 리스트의 길이를 비트 연산을 적용하면, 조합의 갯수가 된다.
        # list길이가 2이면, 조합의 종류는 4가지
        # 길이가 3이면, 조합의 종류는 8가지
        # 길이가 4이면, 조합의 종류는 16가지가 된다. 다 2에 길이승을 하면 조합의 갯수
        print(1 << len(nums), '1--> 100')
        print('n은 0부터 3까지')
        load = []
        for n in range(1 << len(nums)):
            term = 0
            for i in range(len(nums)):
                print('n:', n)
                if n & 1:
                    term ^= nums[i]
                n >>= 1
            result += term
            load.append(term)
        print(load)
        return result


a = Solution()
ex = [1, 3]
print(a.subsetXORSum(ex))
print(a.subsetXORSum_bit(ex))
