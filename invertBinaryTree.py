# Definition for a binary tree node.

from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None

        #swap case
        temp=root.right
        root.right=root.left
        root.left=temp

        self.invertTree(root.right)   
        self.invertTree(root.left)

        return root    
    