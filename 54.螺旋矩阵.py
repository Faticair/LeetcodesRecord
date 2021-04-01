#
# @lc app=leetcode.cn id=54 lang=python3
#
# [54] 螺旋矩阵
#

# @lc code=start
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 取一行，然后逆时针旋转
        # 逆时针旋转：将矩阵倒置后取反
        # 顺时针旋转：将矩阵取反后倒置
        # 取反：new_m = m[::-1]
        # 倒置：new_m = list(map(list, zip(*m)))

        # 学习zip的用法，可以用于求解公共子前缀
        
        res = []
        while matrix:
            res += matrix.pop(0)
            matrix = list(map(list, zip(*matrix)))[::-1]
        return res

# @lc code=end

