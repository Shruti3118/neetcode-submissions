# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = dummy = ListNode(0)
        trailing = 0
        while l1 and l2:
            value = (l1.val+l2.val+trailing)%10
            trailing = (l1.val + l2.val+trailing)//10
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next
            l2 = l2.next
        while l1:
            value = (l1.val + trailing)%10
            trailing = (l1.val + trailing)//10
            curr.next = ListNode(value)
            curr = curr.next
            l1 = l1.next
        while l2:
            value = (l2.val+trailing)%10
            trailing = (l2.val+trailing)//10
            curr.next = ListNode(value)
            curr = curr.next
            l2 = l2.next
        if trailing > 0:
            curr.next = ListNode(trailing)
        return dummy.next
            
        


        