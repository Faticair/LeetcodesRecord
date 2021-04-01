#
# @lc app=leetcode.cn id=16 lang=python3
#
# [16] 最接近的三数之和
#

# @lc code=start
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 10000 # keep minimal gap
        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                gap = sum - target
                if gap == 0:
                    return target
                elif gap > 0:
                    r -= 1
                else:
                    l += 1
                if abs(gap) < abs(res):
                    res = gap      
        return target + res
# @lc code=end

