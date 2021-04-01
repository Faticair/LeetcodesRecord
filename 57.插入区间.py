#
# @lc app=leetcode.cn id=57 lang=python3
#
# [57] 插入区间
#

# @lc code=start
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        if len(intervals) < 2:
            return intervals
        intervals.sort(key=lambda x: x[0])
        res = []
        res.append(intervals[0])
        for i in range(1, len(intervals)):
            if intervals[i][0] <= res[-1][1] and intervals[i][1] <= res[-1][1]:
                continue
            elif intervals[i][0] <= res[-1][1] and intervals[i][1] > res[-1][1]:
                res[-1][1] = intervals[i][1]
            else:
                res.append(intervals[i])
        return res

# @lc code=end

