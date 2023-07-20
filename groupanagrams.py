from collections import defaultdict

"""Problem states that you need to put all anagrams of a word into a single list and return 
all the lists possible. Solution is to create a list of 26 elements and the value of all 
elements should be 0 then for a specific string given in the input list you will
increment the position in the 0 list with the number of time's a letter appears in
the string once you get the list make it a tuple and add it as the key of the dictionary 
and the value for it is the string itself, at last return all the values of the dictionary"""

class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        result=defaultdict(list)

        for s in strs:
            count=[0]*26

            for c in s:
                count[ord(c)-ord("a")]+=1
            result[tuple(count)].append(s)
        
        return result.values()        
    
ob=Solution()
print(ob.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))    