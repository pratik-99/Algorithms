class Solution:
    ##Complete this function
    # Function to check if given number n is a power of two.
    def isPowerofTwo(self,n):
        ##Your code here
        if(n==0):
            return False
        elif(n==1):
            return True
        r=2
        while(r<=n):
            if(r==n):
                return True
            r=r*2    
    def isPowerofTwo2(self,n):        
        if(n==0):
            return False
        return (n&(n-1)==0)  # This solution is using bitwise operator

ob=Solution()
print(ob.isPowerofTwo(16))      