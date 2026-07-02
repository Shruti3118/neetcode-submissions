# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        curr1 = head
        curr2 = self.reverseList(slow.next)
        slow.next = None
        dummy = ListNode(0,head)
        while curr2:
            dummy.next = curr1
            curr1 = curr1.next
            dummy = dummy.next
            dummy.next = curr2
            curr2 = curr2.next
            dummy = dummy.next
        dummy.next = curr1

    def reverseList(self,head):
        curr = head
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev