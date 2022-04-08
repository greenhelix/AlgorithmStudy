class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        temp = {}
        for i in range(len(s)):
            temp[indices[i]] = s[i]

        temp = dict(sorted(temp.items()))

        return "".join(temp.values())


# https://leetcode.com/problems/shuffle-string/
s = "codeleet"
indices = [4, 5, 6, 7, 0, 2, 1, 3]
s = "abc"
indices = [0, 1, 2]
