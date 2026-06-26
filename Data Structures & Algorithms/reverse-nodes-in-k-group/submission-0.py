# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        kth = self.kExists(head,k)
        if not kth:
            return head
        curr = head
        prev = None
        count = 1
        while curr and count <= k:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            count += 1
        head.next = self.reverseKGroup(curr,k)
        return prev

    def kExists(self,head,k):
        curr = head
        count = 1
        while curr and count < k:
            curr = curr.next
            count += 1
        return curr        