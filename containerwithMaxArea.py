"""Refer MaxArea.png for better understanding of the question
we are given an array and need to find the area with using the difference 
between the two points as breadth and the minimum of the two selected number 
as the height, solution is done using two pointers left and right by incrementing 
or decrementing the left and right pointers based on which is greater """
class Solution:
    def maxArea(self, height: list[int]) -> int:
        res=0
        l,r=0,len(height)-1

        while l<r:
            area=(r-l)*min(height[l],height[r])
            res=max(res,area)

            if(height[l]>height[r]):   #checking which pointer to be moved left or right
                r-=1
            else:                      #In equal height condition and right greater then left the 
                l+=1                   #else condition works
        return res            
    
ob=Solution()
print(ob.maxArea([1,8,6,2,5,4,8,3,7]))    