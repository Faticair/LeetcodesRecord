#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        length = len(s)
        if length == 0:
            return 0
        
        # 滑动窗口
        left = 0 # 最左边的边界
        record = set() # 集合保存已经有的元素
        max_length = 0
        cur_length = 0
        for i in range(length):
            cur_length += 1
            while s[i] in record:
                record.remove(s[left])
                cur_length -= 1
                left += 1
            max_length = max(max_length, cur_length)
            record.add(s[i])
        return max_length
        
#  滑动窗口题目:
# 3. 无重复字符的最长子串
# 30. 串联所有单词的子串
# 76. 最小覆盖子串
# 159. 至多包含两个不同字符的最长子串
# 209. 长度最小的子数组
# 239. 滑动窗口最大值
# 567. 字符串的排列
# 632. 最小区间
# 727. 最小窗口子序列

# @lc code=end

