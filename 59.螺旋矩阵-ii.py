#
# @lc app=leetcode.cn id=59 lang=python3
#
# [59] 螺旋矩阵 II
#

# @lc code=start
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n == 1:
            return [[1]]
        matrix = [[0]*n for i in range(n)]
        row, step =0, n - 1
        i = 1
        res_n = n
        while i < n * n + 1:
            for s in range(row, row + step):
                matrix[row][s] = i
                i += 1
            matrix = list(map(list, zip(*matrix)))[::-1]
            if matrix[row][row] != 0:
                row += 1
                res_n = res_n - 2
                step = res_n - 1 if res_n != 1 else 1
        if n % 2 == 1:
            matrix = list(map(list,zip(*matrix[::-1])))
        return matrix

        # l, r, t, b = 0, n - 1, 0, n - 1
        # mat = [[0]*n for i in range(n)]
        # num, tar = 1, n * n
        # while num <= tar:
        #     for i in range(l, r + 1): # left to right
        #         mat[t][i] = num
        #         num += 1
        #     t += 1
        #     for i in range(t, b + 1): # top to bottom
        #         mat[i][r] = num
        #         num += 1
        #     r -= 1
        #     for i in range(r, l - 1, -1): # right to left
        #         mat[b][i] = num
        #         num += 1
        #     b -= 1
        #     for i in range(b, t - 1, -1): # bottom to top
        #         mat[i][l] = num
        #         num += 1
        #     l += 1
        # return mat

# @lc code=end

