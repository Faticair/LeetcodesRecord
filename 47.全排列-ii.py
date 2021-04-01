#
# @lc app=leetcode.cn id=47 lang=python3
#
# [47] 全排列 II
#

# @lc code=start
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        length = len(nums)
        if length < 2:
            return [nums]
        def recursion(tmp, flag):
            if len(tmp) == length:
                res.append(tmp[:])
                return 
            for i in range(0, length):
                if flag[i]:
                    continue
                elif i > 0 and nums[i] == nums[i - 1] and not flag[i - 1]: # 上一个重复数字已经使用所以并不会产生重复结果
                    continue
                else:
                    tmp.append(nums[i])
                    flag[i] = True
                    recursion(tmp, flag)
                    tmp.pop()
                    flag[i] = False
        nums.sort()
        flag = [False for x in range(length)]
        recursion([], flag)
        return res

# @lc code=end

