# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = ListNode(0, head.next)
        node = head
        prev = None
        while node and node.next:
            nxt = node.next
            node.next, nxt.next = nxt.next, node
            if prev:
                prev.next = nxt
            
            prev = node
            node = node.next
        return dummy.next