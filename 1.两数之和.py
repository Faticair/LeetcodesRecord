#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
        if length < 2:
            return []
        res = []
        for i in range(0, length):
            if i == length - 1:
                break
            for j in range(i+1, length):
                if nums[i] + nums[j] == target:
                    res.append(i)
                    res.append(j)
                    return res
        return []

        # 字典做法，时间复杂度O（logn）
        # hashmap = {}
        # for index, num in enumerate(nums):
        #     another_num = target - num
        #     if another_num in hashmap:
        #         return [hashmap[another_num], index]
        #     hashmap[num] = index
        # return None
        
# @lc code=end

