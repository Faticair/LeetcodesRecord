#
# @lc app=leetcode.cn id=58 lang=python3
#
# [58] 最后一个单词的长度
#

# @lc code=start
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        res = 0
        i = len(s) - 1

        while i >= 0:
            flag = False
            while i >= 0 and s[i] != ' ':
                flag = True
                res += 1
                i -= 1
            i -= 1
            if flag:
                break
        
        return res
# @lc code=end

