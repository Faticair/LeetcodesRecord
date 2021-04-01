#
# @lc app=leetcode.cn id=39 lang=python3
#
# [39] 组合总和
#

# @lc code=start
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        res = []
        candidates.sort()
        def recurtion(numlist, tar, index):
            if tar == 0:
                res.append(numlist[:])
                return
            else:
                for num in candidates:
                    if tar - num < 0:
                        return 
                    if num >= index:
                        numlist.append(num)
                        recurtion(numlist, tar - num, num)
                        numlist.pop()
        recurtion([], target, 0)
        
        return res

# @lc code=end

