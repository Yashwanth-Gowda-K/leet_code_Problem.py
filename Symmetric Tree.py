from typing import Optional

class Solution:
    def isSymetric(seld , root:Optional[TreeNode]) -> bool:
        def isMirror(t1, t2):
            if not t1 and not t2: # Both nodes are None -> They match
                return True
            if not t1 or not t2: # One is None , the other isn't -> They Dont match
                return False
            
            return(t1.val == t2.val and 
                   isMirror(t1.left, t2.right)and
                   isMirror(t1.right , t2.left))
        #Comaparing left and right from the root
        return isMirror(root, root)