""""""

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq={}
        countlst=[[] for i in range(len(nums)+1)]
        for i in nums:
            freq[i]=1+freq.get(i,0)

        for c,v in freq.items():
            countlst[v].append(c)
        #print(countlst)
        res=[]
        for j in range(len(nums),0,-1):
            print(j)
            for n in countlst[j]:
                res.append(n)
                if(len(res)==k):
                    return res
                
ob=Solution()
print(ob.topKFrequent([1,1,1,1,1,1],1))                