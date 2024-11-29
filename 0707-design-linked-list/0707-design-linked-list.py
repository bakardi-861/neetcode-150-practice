class ListNode:
    def __init__(self,x): 
        self.val = x
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = ListNode(-1) # dummy node
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            print(f"get({index}): index is invalid")
            return -1

        curr = self.head
        for _ in range(index+1):
            curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0,val)
        
    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size,val)

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        if index < 0:
            index = 0
        
        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        node = ListNode(val)
        node.next = prev_node.next # set node.next = rest of the list
        prev_node.next = node # set prev.next = new node
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            print(f"deleteAtIndex({index}): index is invalid")
            return

        prev_node = self.head
        for _ in range(index):
            prev_node = prev_node.next

        prev_node.next = prev_node.next.next
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)