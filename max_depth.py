"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root: 
            return 0
        
        max_child_depth = 0
        for child in root.children:  
            current_depth = self.maxDepth(child) 
            if current_depth > max_child_depth:
                max_child_depth = current_depth
        
        return 1 + max_child_depth  
