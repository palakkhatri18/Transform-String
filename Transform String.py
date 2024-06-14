# Given two strings A and B. Find the minimum number of steps required to transform string A into string B. The only allowed operation for the transformation is selecting a character from string A and inserting it in the beginning of string A.
from collections import Counter
class Solution:
    def transform(self, A, B):
        if len(A) != len(B):
            return -1
        
        # Check if both strings have the same characters with the same frequencies
        if Counter(A) != Counter(B):
            return -1
        
        count = 0
        i = len(A) - 1
        j = len(B) - 1
        
        while i >= 0 and j >= 0:
            if A[i] != B[j]:
                count += 1
                i -= 1
            else:
                i -= 1
                j -= 1
        
        return count