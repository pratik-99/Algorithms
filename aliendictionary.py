
#Topological search/ Depth first search (DFS)

def findOrder(alien_dict, N, K):
    # code here
        adj={c:set() for words in alien_dict for c in words}
    
        for i in range(N-1):
            w1, w2= alien_dict[i], alien_dict[i+1]
            minlen=min(len(w1),len(w2))
            #check if word1 length is greater than word2 with same prefix and different ending and placed before word2
            #rat, rate --> rat should be placed before rate
            if(len(w1)>len(w2) and w1[:minlen]==w2[:minlen]):  
                return ""
           # print(minlen)    
            for j in range(minlen):
                if w1[j]!=w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        print(adj)        
        visited={}
        res=[]
        def dfs(char):
                if char in visited:
                    return visited[char]
    
                visited[char] = True
    
                for neighChar in adj[char]:
                    if dfs(neighChar):
                        return True
    
                visited[char] = False
                res.append(char)
    
        for char in adj:
            if dfs(char):
                return ""
        print(visited)
        res.reverse()
        return "".join(res)
        
print(findOrder(["baa", "abcd", "abca", "cab" ,"cada"],5,4))        