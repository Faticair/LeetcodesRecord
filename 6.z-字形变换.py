#
# @lc app=leetcode.cn id=6 lang=python3
#
# [6] Z 字形变换
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) < numRows or numRows == 1:
            return s
        res = ""
        f = numRows - 1
        length = len(s)
        for n in range(numRows):
            k = n
            while k < length:
                res += s[k]
                k += 2 * f
                if n != 0 and n != f and k - 2 * n < length:
                    res += s[k-2*n]
        return res
        
# @lc code=end

