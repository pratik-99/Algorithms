#Program to find pallindrome in substring using sliding window using dp
#(sliding window part written by me)
#code works but not very efficient

def longestPalin( S):
    n=len(S)
    dp = [[False] * n for _ in range(n)]
    maxlen=0
    lsubstr=""
    val=True
    for i in range(n):
        dp[i][i]=True
        lsubstr=S[i:i]
        
    for i in range(n-1):
        if(S[i]==S[i+1]):
            dp[i][i+1]=True
            if(val):
                lsubstr=S[i:i+2]
                val=False
            #print(lsubstr) 
            maxlen=2
    
    l=0
    r=1 
    slider=1               
    while(slider<n ):
        while(r<n and l<n):
            if (S[l]==S[r] and dp[l+1][r-1]==True):
                dp[l][r]=True
                if(r-l+1>maxlen):
                    maxlen=r-l+1
                    lsubstr=S[l:r+1]
            r+=1
            l+=1
        r=0    
        slider+=1
        l=0
        r+=slider
                
                
    
    return lsubstr
    
print(longestPalin("ac")) 