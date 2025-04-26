"""
Given an array of integers numbers that is sorted in non-decreasing order.

Return the indices (1-indexed) of two numbers, [index1, index2], 
such that they add up to a given target number target and index1 < index2.
Note that index1 and index2 cannot be equal, therefore you may not use the same element twice.

There will always be exactly one valid solution.

Example:
    Input: numbers = [1,2,3,4], target = 3

    Output: [1,2]
"""
from typing import List
# Brute Force 

def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            for j in range(i+1,len(numbers)):
                if(numbers[i]+numbers[j]>target):
                    break
                if(numbers[i]+numbers[j]==target):
                    return [i+1,j+1]
#Two Pointer method

def twoSumTwoPointer(self, numbers:List[int], target: int):
    l=0
    r=len(numbers)-1
    while l<r:
        if(numbers[l] + numbers[r] < target):
            l+=1 
            
        elif(numbers[l]+numbers[r]>target):
            r-=1
        else:
            return [l+1,r+1]                   