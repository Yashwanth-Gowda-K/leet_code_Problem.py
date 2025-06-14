# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        if not root:
            return False
        
        if root.val == x or root.val == y:
            return False
        
        x_depth = -1
        y_depth = -1
        x_parent = None
        y_parent = None

        queue = deque ()
        queue.append((root , None , 0))

        while queue:
            current , parent , depth = queue.popleft()

            if current.val == x:
                x_depth = depth
                x_parent = parent

            elif current.val == y:
                y_depth = depth
                y_parent = parent
            
            if x_depth != -1 and y_depth != -1:
                break
            
            if current.left:
                queue.append((current.left , current, depth +1))
            if current.right:
                queue.append((current.right , current , depth +1))
        return x_depth == y_depth and x_parent != y_parent
