# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:                 #If the subroot which we need to check in the root node is null then 
            return True                 # by default it is present in the root node so return true
        if not root:
            return False                #If root node is null then directly return false as subroot cannot be checked for it.
        if(self.isSametree(root,subRoot)):
            return True
        return self.isSubtree(root.right,subRoot) or self.isSubtree(root.left,subRoot)

    def isSametree(self,root, subroot):
        if not root and not subroot:
            return True
        if root and subroot and root.val==subroot.val:
            return (self.isSametree(root.left,subroot.left) and 
                   self.isSametree(root.right,subroot.right))
        return False