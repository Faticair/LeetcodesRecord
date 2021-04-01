#
# @lc app=leetcode.cn id=22 lang=python3
#
# [22] 括号生成
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def recursion(s, l_n, r_n):
            if l_n == n:
                if r_n == n:
                    res.append(s)
                    return
                else:
                    recursion(s + ')', l_n, r_n + 1)
            else:
                recursion(s + '(', l_n + 1, r_n)
                if l_n > r_n:
                    recursion(s + ')', l_n, r_n + 1)
        
        recursion('', 0, 0)
        return res

# @lc code=end


