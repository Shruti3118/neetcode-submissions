"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return
        curr = head
        while curr:
            temp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = temp
            curr = curr.next.next
        curr = head
        while curr and curr.next:
            curr.next.random = curr.random.next if curr.random else None
            curr = curr.next.next
        head1 = head.next
        curr1 = head1
        curr = head
        while curr and curr.next:
            curr1 = curr.next
            curr.next = curr.next.next
            curr1.next = None if not curr1.next else curr1.next.next
            curr = curr.next
            curr1 = curr1.next
        return head1

        