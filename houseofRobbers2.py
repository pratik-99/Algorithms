"""Similar to houseofRobbers1 just with a twist
Given a circular array you can add any of the numbers in the array except the adjacents ones
the first and last numbers are adjacent to each other as well 
find a sum in the array which is maximum """
"""This is solved using DP
suppose an array [2,7,9,3,1] then you need check the houseofRobbers algo
in the array in 2 parts 1st one is the entire array excluding last element
2nd is the entire array except the 1st element and check for maximum amongst these 2 numbers
The output is 11 """
class Solution:
    def rob(self, nums: list[int]) -> int:
        return max(nums[0],self.helper(nums[1:]),self.helper(nums[:-1]))


    def helper(self,nums):
        rob1,rob2=0,0

        for i in nums:
            temp=max(i+rob1,rob2)
            rob1=rob2
            rob2=temp
        return rob2        
ob=Solution()
print(ob.rob([2,7,9,3,1]))    