#
# @lc app=leetcode.cn id=70 lang=python3
#
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        # Time Exceed
        # if n == 1 or n == 2:
        #     return n
        # return self.climbStairs(n - 1) + self.climbStairs(n - 2)

        if n == 1 or n == 2:
            return n
        a, b = 1, 2
        sum = 0
        for i in range(3,n + 1):
            sum = a + b
            a = b
            b = sum
        return sum


# @lc code=end

