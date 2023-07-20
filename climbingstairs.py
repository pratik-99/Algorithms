"""You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
"""
"""This problem is basically solved using fibonacci algorithm"""

class Solution:
    def climbStairs(self, n: int) -> int:
        step1, step2= 1,1
        for i in range(n-1):
            temp=step1
            step1=step1+step2
            step2=temp
        return step1    
    
ob=Solution()
print(ob.climbStairs(6))    