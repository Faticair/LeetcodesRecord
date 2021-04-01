#
# @lc app=leetcode.cn id=209 lang=python3
#
# [209] 长度最小的子数组
#

# @lc code=start
class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        if sum(nums) < s:
            return 0
        count = len(nums)
        min_len = count
        left = 0
        right = left
        remain = s - nums[left]
        if remain < 0: return 1
        while right < count:
            if remain > 0:
                right += 1
                if right == count:
                    break
                remain -= nums[right]
            else:
                min_len = min(min_len, right - left + 1)
                remain += nums[left]
                left += 1
                if left > right: return 1
        return min_len

# @lc code=end

