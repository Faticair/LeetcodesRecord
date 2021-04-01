#
# @lc app=leetcode.cn id=14 lang=python3
#
# [14] 最长公共前缀
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        count = len(strs)
        if count == 0:
            return ""
        if count == 1:
            return strs[0]
        res = ""
        s0 = min(strs)
        s1 = max(strs)
        length = min(len(s0), len(s1))
        for i in range(length):
            if s0[i] == s1[i]:
                res += s0[i]
            else:
                break
        return res
# @lc code=end

