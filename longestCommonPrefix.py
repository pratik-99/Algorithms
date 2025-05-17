"""
Longest Common Prefix

You are given an array of strings strs. Return the longest common prefix of all the strings.

If there is no longest common prefix, return an empty string "".

Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings."""
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=''
        for i in range(len(strs[0])):
            for j in strs:
                if(i==len(j) or strs[0][i]!= j[i]):
                    return res
            res+=strs[0][i]
        return strs[0]            
print(Solution().longestCommonPrefix(["dog","racecar","car"]))