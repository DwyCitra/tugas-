# -*- coding: utf-8 -*-
"""LongestCommon.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1lzjcm9pPTsQMjlV7nletl2sCa6ME0U6g
"""

# Longest Common Subsequence in Python

def findLCS(s1, s2, index1, index2):
    if index1 == len(s1) or index2 == len(s2):
        return 0
    if s1[index1] == s2[index2]:
        return 1 + findLCS(s1, s2, index1+1, index2+1)
    else:
        op1 = findLCS(s1,s2, index1, index2+1)
        op2 = findLCS(s1,s2, index1+1, index2)
        return max(op1, op2)

print(findLCS("elephant", "eretpat", 0, 0))

