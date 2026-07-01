# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = curr = ListNode()
        while True:
            mini = self.getMinimumNode(lists)
            if mini.val == float('inf'):
                return dummy.next
            for i in range(len(lists)):
                if lists[i] and lists[i].val == mini.val:
                    curr.next = lists[i]
                    curr = curr.next
                    lists[i]= lists[i].next


    
    def getMinimumNode(self,lists):
        mini = ListNode(float('inf'))
        for i in range(len(lists)):
            if lists[i] and mini.val > lists[i].val:
                mini = lists[i]
        return mini

