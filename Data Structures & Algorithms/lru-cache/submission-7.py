class Node:
    def __init__(self,key,value):
        self.hm = {}
        self.hm[key] = value
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = None

    def get(self, key: int) -> int:
        curr = self.head
        prev = None
        while curr:
            if key in curr.hm:
                if not prev:
                    return curr.hm[key]
                prev.next = None if not curr.next else prev.next.next
                curr.next = self.head
                self.head = curr
                return curr.hm[key]
            prev = curr    
            curr = curr.next
        return -1     

    def put(self, key: int, value: int) -> None:
        if self.capacity == 1:
            self.head = Node(key,value)
            return            
        if self.get(key) != -1:
            curr = self.head
            prev = None
            while curr:
                if key in curr.hm:
                    if not prev:
                        curr.hm[key] = value
                        return
                    prev.next = None if not curr.next else prev.next.next
                    curr.hm[key] = value
                    curr.next = self.head
                    self.head = curr
                    return
                prev = curr
                curr = curr.next
        newNode = Node(key,value)
        self.size += 1
        if self.size > self.capacity:
            curr = self.head
            prev = None
            while curr.next:
                prev = curr
                curr = curr.next
            prev.next = None
            self.size -= 1    
        newNode.next = self.head
        self.head = newNode
