#
# @lc app=leetcode.cn id=17 lang=python3
#
# [17] 电话号码的字母组合
#

# @lc code=start


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        dic = {
            '2':'abc', 
            '3':'def', 
            '4':'ghi',
            '5':'jkl', 
            '6':'mno',
            '7':'pqrs',
            '8':'tuv', 
            '9':'wxyz'
        }
        res = []

        def recursion(s, tmp):
            if s == "":
                res.append(tmp)
                return
            for letter in dic[s[0]]:
                recursion(s[1:], tmp + letter)

        recursion(digits, '')

        return res    
            
# @lc code=end

