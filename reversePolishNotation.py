"""
Evaluate Reverse Polish Notation
You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

Return the integer that represents the evaluation of the expression.

The operands may be integers or the results of other operations.
The operators include '+', '-', '*', and '/'.
Assume that division between integers always truncates toward zero.

Example 1:
Input: tokens = ["1","2","+","3","*","4","-"]

Output: 5

Explanation: ((1 + 2) * 3) - 4 = 5

Example 2:
Input: tokens = ["4","13","5","/","+"]
Output: 6

Explanation: (4 + (13 / 5)) = 6
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                stack.append(stack.pop() + stack.pop())
            elif i == "-":
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            elif i == "*":
                stack.append(stack.pop() * stack.pop())
            elif i == "/":
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            else:
                stack.append(int(i))
        return stack.pop()