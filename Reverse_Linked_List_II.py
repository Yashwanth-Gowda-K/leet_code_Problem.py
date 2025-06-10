# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        # Edge case: empty list
        if not head:
            return None
        
        # Step 1: Create a dummy node to handle cases where left = 1
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        # Step 2: Move prev to the node just before the reversal starts (left-1)
        for _ in range(left - 1):
            prev = prev.next
        
        # Step 3: Initialize pointers for reversal
        curr = prev.next  # First node to be reversed
        next_node = None
        
        # Step 4: Reverse the segment between left and right
        for _ in range(right - left):
            next_node = curr.next
            curr.next = next_node.next
            next_node.next = prev.next
            prev.next = next_node
        
        # Step 5: Return the modified list (skip the dummy node)
        return dummy.next
