class Solution(object):
    def lengthOfLongestSubstring(self, s):
        dic, res, j = {}, 0, 0
        for i in range(len(s)):
            if s[i] not in dic:
                dic[s[i]] = i
            else:
                j = max(j, dic[s[i]]+1)
                dic[s[i]] = i
            res = max(res, i-j+1)
        return res
