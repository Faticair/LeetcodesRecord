#
# @lc app=leetcode.cn id=7 lang=python3
#
# [7] 整数反转
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            flag = -1
        else:
            flag = 1
        tmp = str(abs(x))
        res = flag * int(tmp[::-1])
        if res >= -2**31 and res < 2**31-1:
            return res
        else:
            return 0

# @lc code=end

