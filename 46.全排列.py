#
# @lc app=leetcode.cn id=46 lang=python3
#
# [46] 全排列
#

# @lc code=start
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) < 2:
            return [nums]
        res = []

        def recursion(tmp):
            if len(tmp) == len(nums):
                res.append(tmp[:])
                return 
            for num in nums:
                if num in tmp:
                    continue
                else:
                    tmp.append(num)
                    recursion(tmp)
                    tmp.pop()
        
        recursion([])
        return res
# @lc code=end

