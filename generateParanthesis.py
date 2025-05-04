"""
You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

Example 1:
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]

Example 2:
Input: n = 1
Output: ["()"]
"""

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        res = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2*n:
                res.append(S)
                return
            if left < n:
                backtrack(S + '(', left + 1, right)
            if right < left:
                backtrack(S + ')', left, right + 1)
        backtrack()
        return res

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack=[]
        res=[]
        # only add open parenthesis if open < n
        # only add close parenthesis if close < open
        # valid if open == close == n
        def dfs (openB, closeB):
            if openB == closeB == n:
                res.append("".join(stack))
                return
            if openB < n:
                stack.append('(')
                dfs(openB+1, closeB)
                stack.pop()
            if closeB < openB:
                stack.append(')')
                dfs(openB, closeB+1)
                stack.pop()

        dfs(0,0)
        return res         