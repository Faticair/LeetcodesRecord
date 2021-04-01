#
# @lc app=leetcode.cn id=75 lang=python3
#
# [75] 颜色分类
#

# @lc code=start
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        left, right = 0, length - 1
        p = 0
        while p <= right:
            if nums[p] == 0:
                nums[left], nums[p] = nums[p], nums[left]
                left += 1
                p += 1
            elif nums[p] == 2:
                nums[right], nums[p] = nums[p], nums[right]
                right -= 1
            else:
                p += 1
            

# @lc code=end

