"""
Koko Eats Banana
You are given an integer array piles where piles[i] is the number of bananas in the ith pile. 
You are also given an integer h, which represents the number of hours you have to eat all the bananas.

You may decide your bananas-per-hour eating rate of k. 
Each hour, you may choose a pile of bananas and eats k bananas from that pile. 
If the pile has less than k bananas, you may finish eating the pile but you can not eat from another pile in the same hour.

Return the minimum integer k such that you can eat all the bananas within h hours.

Example 1:
Input: piles = [3,6,7,11], h = 8
Output: 4

Example 2:
Input: piles = [30,11,23,4,20], h = 5
Output: 30

Example 3:
Input: piles = [30,11,23,4,20], h = 6
Output: 23
"""

class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l, r= 1, max(piles)
        res= r
        while l<=r:
            k= (l+r)//2
            total=0
            for p in piles:
                total+= math.ceil(float(p)/k)

            if total<=h:
                res= k
                r= k-1
            else:
                l= k+1        
        return res