class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # Inner function to check if two trees are mirror images
        def isMirror(t1, t2):
            # Case 1: both nodes are None → symmetric here
            if not t1 and not t2:
                return True
            
            # Case 2: one is None, one isn't → not symmetric
            if not t1 or not t2:
                return False
            
            # Case 3: check values and recurse on children in mirrored order
            return (
                t1.val == t2.val and                       # values must match
                isMirror(t1.left, t2.right) and            # outer children match
                isMirror(t1.right, t2.left)                # inner children match
            )
        
        # Start comparing left and right from the root
        return isMirror(root, root)
