#
# @lc app=leetcode.cn id=40 lang=python3
#
# [40] 组合总和 II
#

# @lc code=start
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        if candidates == []:
            return []
        candidates.sort()
        res = []
        length = len(candidates)

        def recursion(numlist, tar, index):
            if tar == 0:
                # if numlist in res:
                #     return 
                res.append(numlist[:])
                return 
            elif index == length:
                return
            else:  # index为函数层级，i为迭代指针
                for i in range(index, length):
                    if tar - candidates[i] < 0:
                        return
                    # 每个i导致新的分支出现，为了剪枝要对i进行判断
                    if i > index and candidates[i] == candidates[i - 1]:
                        continue
                    numlist.append(candidates[i])
                    recursion(numlist, tar - candidates[i], i + 1)
                    numlist.pop()
        
        recursion([], target, 0)
        return res
# @lc code=end

