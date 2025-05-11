"""
Find First and Last Position of Element in Sorted Array

You are given a non-decreasing array 'arr' consisting of 'n' integers and an integer 'x'. 
You need to find the first and last position of 'x' in the array.

Note:
1. The array follows 0-based indexing, so you need to return 0-based indices.
2. If 'x' is not present in the array, return {-1 -1}.
3. If 'x' is only present once in the array, the first and last position of its occurrence will be the same.

Example:
Input:  arr = [1, 2, 4, 4, 5],  x = 4

Output: 2 3
"""
def searchRange(arr: [int], x: int) -> [int]:
    def leftBinarySearch(arr, x):
        left, right = 0, len(arr)-1
        first =-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == x:
                first= mid
                right = mid-1
            elif arr[mid] < x:
                left = mid+1
            else:
                right = mid-1
        return first
    def rightBinarySearch(arr, x):
        left, right = 0, len(arr)-1
        last =-1
        while left <= right:
            mid = (left+right)//2
            if arr[mid] == x:
                last= mid
                left = mid+1
            elif arr[mid] < x:
                left = mid+1
            else:
                right = mid-1
        return last
    return [leftBinarySearch(arr, x), rightBinarySearch(arr, x)]    