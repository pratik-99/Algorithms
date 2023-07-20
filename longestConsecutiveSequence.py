"""The idea behind the solution is to check if a number 
smaller then the current number exists in the array
if not then take this as the starting point of longest 
sequence, then keeping on adding 1 and checking if the
number exists in the sequence if yes then increment length
at last compare length and current longest sequence to find
the longest sequence"""

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        seq=set(nums)
        longest=0

        for i in range(len(nums)):
            if(nums[i]-1 not in seq):
                length=0
                while(nums[i]+length in seq):
                    length+=1
                longest=max(longest,length)   
        return longest         
ob=Solution()    
print(ob.longestConsecutive([100,4,200,3,2,1]))    
