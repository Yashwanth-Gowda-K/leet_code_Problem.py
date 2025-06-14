"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        # Base case: if tree is empty
        if not root:
            return []
        
        # Start with root's value
        result = [root.val]
        
        # Recursively traverse all children
        for child in root.children:
            result += self.preorder(child)  # Note: using self.preorder
            
        return result
