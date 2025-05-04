"""
Daily Temperatures
You are given an array of integers temperatures where temperatures[i] represents the daily temperatures on the ith day.

Return an array result where result[i] is the number of days after the ith day before a warmer temperature appears on a future day. 
If there is no day in the future where a warmer temperature will appear for the ith day, set result[i] to 0 instead.

Example 1:
Input: temperatures = [30,38,30,36,35,40,28]
Output: [1,4,1,2,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]
"""

class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        res = [0] * len(temperatures)
        stack = []  # pair: [temp, index]

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                stackT, stackInd = stack.pop()
                res[stackInd] = i - stackInd
            stack.append((t, i))
        return res

class MySolution:        
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        j=0
        for i in range(len(temperatures)):
            if(j==len(temperatures)-1 and i!=len(stack)):
                stack.append(0)
            for j in range(i+1,len(temperatures)):
                if(temperatures[j]>temperatures[i]):
                    stack.append(j-i)
                    break
        stack.append(0) 
        return stack