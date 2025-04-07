# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # Both nodes are None -> They match
            return True
        if not p or not q: # One is None , the other isn't -> They Dont match
            return False
        if p.val !=q.val:
            return False
        
        # Recursively Checking left and right childern
        return self.isSameTree(p.left , q.left) and self.isSameTree(p.right, q.right)

        