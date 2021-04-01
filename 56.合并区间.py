#
# @lc app=leetcode.cn id=56 lang=python3
#
# [56] 合并区间
#

# @lc code=start
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            # if intervals[i][0] <= res[-1][1]:
                # tmp = res.pop()
                # if tmp[1] > intervals[i][1]:
                #     res.append(tmp)
                # else:
                #     res.append([tmp[0], intervals[i][1]])
            if intervals[i][0] <= res[-1][1] and intervals[i][1] <= res[-1][1]:
                continue
            elif intervals[i][0] <= res[-1][1] and intervals[i][1] > res[-1][1]:
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res
# @lc code=end

