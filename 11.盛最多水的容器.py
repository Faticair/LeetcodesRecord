#
# @lc app=leetcode.cn id=11 lang=python3
#
# [11] 盛最多水的容器
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        column = len(height)
        if column < 2:
            return 0
        if column == 2:
            return min(height)
        res = 0
        left = 0
        right = column - 1
        while left < right:
            tmp = min(height[left], height[right]) * (right - left)
            res = max(res, tmp)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return res


# @lc code=end

