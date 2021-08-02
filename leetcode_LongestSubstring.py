# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #建立一個空集合
        aset = set()
        #回傳結果
        result = 0
        #左指標
        left = 0
        #右指標
        right = 0
        #假設字串小於1 那就直接回傳長度
        if len(s) < 1:
            return result
        #字串長度有多少,就依序去比對每個字
        for right in range(len(s)):
            #如果該字已經存在於set裡面,那就移除左指標
            #並且左指標位置+1
            while s[right] in aset:
                aset.remove(s[left])
                left +=1
            #如果該字不存在於set裡面,就寫入該字
            aset.add(s[right])
            
            #結果 = 取最大長度
            #當前"字"長度跟紀錄的"字"長度誰比較大,比較大的就記錄下來
            #右指標-左指標 要記得+1才會是實際上的 字串長度
            result = max(result,right-left+1)
        return result
            
