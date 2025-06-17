from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node):
            nonlocal curr
            if not node:
                return
            dfs(node.left)
            node.left = None
            curr.right = node
            curr = node
            dfs(node.right)
        
        dummy = TreeNode(-1)
        curr = dummy
        dfs(root)
        return dummy.right
