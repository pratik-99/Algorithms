"""Given an array you can add any of the numbers in the array except the adjacents ones find a sum in the array which is maximum"""
"""This is solved using DP
suppose an array [2,7,9,3,1] then the 
max array computes to be[2,7,11,11,12]
The output is 12 """
class Solution:
    def rob(self, nums: list[int]) -> int:
        if(len(nums)<2):
            return nums[0]
        rob1=nums[0]
        rob2=max(nums[0],nums[1])
        for n in nums[2:]:
            temp=max(n+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2    
    
ob=Solution()
print(ob.rob([2,7,9,3,1]))
