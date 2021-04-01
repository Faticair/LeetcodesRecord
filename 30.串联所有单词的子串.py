#
# @lc app=leetcode.cn id=30 lang=python3
#
# [30] 串联所有单词的子串
# 思路：
# 单词长度相同且只出现一次，每个给定的单词列表有n！种可能搭配
# 使用滑动窗口（n个长为l的单词），每次读入一个单词，滑动一个单词

# !!!可能存在words中存在重复单词，使用字典来记录读入的单词
# !!!字符串中单词长度并不相同，考虑截取固定长度字串逐一判断

# @lc code=start
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if s == '' or words == []:
            return []
        word_length = len(words[0])
        word_count = len(words)
        word_dic = {}
        res = []
        for word in words:
            if word in word_dic:
                word_dic[word] += 1
            else:
                word_dic[word] = 1

        sub_s_len = word_count * word_length
        if sub_s_len > len(s):
            return []
        for i in range(0, len(s)-sub_s_len+1):
            dic_copy = word_dic.copy()
            flag = True
            for p in range(i,i+sub_s_len,word_length):
                w = s[p:p+word_length]
                if w in words and dic_copy[w] != 0:
                    dic_copy[w] -= 1
                else: 
                    flag = False
                    break
            if flag:
                res.append(i)
        return res


# @lc code=end

