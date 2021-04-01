#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        mid = (length1 + length2) // 2
        flag = (length1 + length2) % 2
        new_nums = nums1 + nums2
        new_nums.sort()
        if flag == 1:
            return float(new_nums[mid])
        else:
            res = (new_nums[mid] + new_nums[mid-1]) / 2
            return res
       
# @lc code=end

