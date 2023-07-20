class Solution:
    def twoSumMy(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                if(nums[i]+nums[j])==target:
                    return (i,j)
                
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        prevMap={}
        for i, n in enumerate(nums):
            diff=target-n
            if diff in prevMap:
                return (prevMap[diff],i)
            prevMap[n]=i            


ob=Solution()
print(ob.twoSum([1,2,3],5))            