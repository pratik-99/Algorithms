def maxSubArraySum(arr,N):
        ##Your code here
        cursum=0
        maxsum=arr[0]
        for i in arr:
            if(cursum<0):
                cursum=0
            cursum+=i
            maxsum=max(cursum,maxsum)
            
        return maxsum    

print(maxSubArraySum([1,2,3,-7,5,6],6))