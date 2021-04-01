#
# @lc app=leetcode.cn id=8 lang=python3
#
# [8] 字符串转换整数 (atoi)
#

# @lc code=start
INT_MAX = 2 ** 31 - 1
INT_MIN = -2 ** 31

class Auto:
    def __init__(self):
        self.table = [
            ['start', 'num', 'signed', 'end'],
            ['end', 'num', 'end', 'end'], 
            ['end', 'num', 'end', 'end'], 
            ['end', 'end', 'end', 'end']
        ]
        self.state = 'start'
        self.res = 0
        self.sign = 1

    def row(self):
        if self.state == 'start':
            return 0
        elif self.state == 'num':
            return 1
        elif self.state == 'signed':
            return 2
        else:
            return 3

    def col(self, c):
        if c.isspace():
            return 0
        elif c.isdigit():
            return 1
        elif c == '+' or c == '-':
            return 2
        else:
            return 3

    def get_state(self, c):
        self.state = self.table[self.row()][self.col(c)]
        if self.state == 'num':
            self.res = self.res * 10 + int(c)
        elif self.state == 'signed':
            self.sign = -1 if c == '-' else 1

class Solution:
    def myAtoi(self, s: str) -> int:
        automation = Auto()
        for c in s:
            automation.get_state(c)
        automation.res = min(automation.res, INT_MAX) if automation.sign == 1 else min(automation.res, -INT_MIN)
        return automation.sign * automation.res
        
       
# @lc code=end

