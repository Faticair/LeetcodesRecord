#
# @lc app=leetcode.cn id=62 lang=python3
#
# [62] 不同路径
#

# @lc code=start
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0] * n for t in range(m)]
        for i in range(m):
            dp[i][0] = 1
        for j in range(n):
            dp[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]


        # Time Limit Exceeded
        # def recursion(i, j):
        #     if i == 0 or j == 0:
        #         return 1
        #     else:
        #         return recursion(i - 1, j) + recursion(i, j - 1)
        
        # return recursion(m - 1, n - 1)
# @lc code=end

