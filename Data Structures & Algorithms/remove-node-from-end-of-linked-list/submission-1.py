# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head.next:
            return None 
        curr = dummy = ListNode(0,head)
        fast = head
        count = 1
        while fast and count < n:
            fast = fast.next
            count += 1
        while fast.next:
            curr = curr.next
            fast = fast.next
        curr.next = curr.next.next
        return dummy.next
