class Solution:
    def isValid(self, s: str) -> bool:
        closedmap={"}":"{", "]":"[", ")":"("}
        stack=[]
        for i in s:
            if i in closedmap:
                if stack and stack[-1]==closedmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if not stack else False                    
    

ob=Solution()    
print(ob.isValid("{{[()]}}"))