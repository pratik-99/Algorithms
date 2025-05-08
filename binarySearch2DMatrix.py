"""Binary Search 2D Matrix
You are given an m x n 2-D integer array matrix and an integer target.

Each row in matrix is sorted in non-decreasing order.
The first integer of every row is greater than the last integer of the previous row.
Return true if target exists within matrix or false otherwise.

Can you write a solution that runs in O(log(m * n)) time?

Example 1: 
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false"""

class Solution:
    # staircase method time complexity O(m+n)
    
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        row=len(matrix)-1
        col=0
        while(row>=0 and col<len(matrix[0])):
            if(matrix[row][col]==target):
                return True
            elif(matrix[row][col]>target):
                row-=1
            else:
                col+=1
        return False


    # binary search method time complexity O(log(m*n)) better approach
    def SearchMatrix2(self, matrix: list[list[int]], target: int) -> bool:
        row_count = len(matrix)
        column_count = len(matrix[0])

        total_number_in_matrix = row_count * column_count
        left = 0
        right = total_number_in_matrix - 1
        
        while left <= right:
            middle = (left + right) // 2
            row_index = middle // column_count
            column_index = middle % column_count

            mid_num = matrix[row_index][column_index]
            if target == mid_num:
                return True
            elif target < mid_num:
                right = middle - 1
            else:
                left = middle + 1
            
        return False       
          