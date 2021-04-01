#
# @lc app=leetcode.cn id=69 lang=python3
#
# [69] x 的平方根
#

# @lc code=start
class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        left = 0
        right = x // 2
        while left < right:
            mid = (left + right) // 2 + 1
            if mid > x // mid:
                right = mid - 1
            else:
                left = mid
        return left

# @lc code=end

