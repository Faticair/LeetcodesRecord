#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2 or s == s[::-1]:
            return s
        res = s[0]
        
        # force
        # max_len = 1
        # for i in range(len(s) - 1):
        #     for j in range(i + 1, len(s)):
        #         if j - i + 1 > max_len and s[i:j+1] == s[i:j+1][::-1]:
        #             max_len = j - i + 1
        #             res = s[i:j + 1]
        # return res


        # 中心扩散
        for i in range(len(s)):
            palindrome_odd= self.spread(s,i, i)
            palindrome_even= self.spread(s,i, i + 1)

            res = max(palindrome_odd,palindrome_even,res,key=len)
        return res

    def spread(self, s, left, right):
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

# @lc code=end

