#
# @lc app=leetcode.cn id=78 lang=python3
#
# [78] 子集
#

# @lc code=start
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        if not nums:
            return res
        length = len(nums)

        def recursion(s, temp):
            res.append(temp)
            for i in range(s, length):
                recursion(i + 1, temp + [nums[i]])

        recursion(0, [])
        return res
# @lc code=end

