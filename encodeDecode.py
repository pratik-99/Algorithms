
"""
Design an algorithm to encode a list of strings to a single string. 
The encoded string is then decoded back to the original list of strings.

Logic: create an encoded string from the given list of strings,
add the length of the string then '#' and then the sting concat till the end of the list
To decode the string loop through the string when you find a # the previous character has to be the length of the string
skip the number and # and store the string in the list
"""
class Solution:

    def encode(self, strs: List[str]) -> str:
        encode_str=""
        for word in strs:
            encode_str+= str(len(word))+"#"+word
        return encode_str    
    def decode(self, s: str) -> List[str]:
        res=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            length=int(s[i:j])
            i=j+1
            j=i+length
            res.append(s[i:j])
            i=j    
        return res