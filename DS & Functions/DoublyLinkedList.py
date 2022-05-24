class DoublyLinkedList:
    def __init__(self, data=None, next=None, prev=None) -> None:
        self.data = data
        self.next = next
        self.prev = prev
    
    def print_forward(self):
        while self != None:
            print(self.data)
            self = self.next
    
    def print_back(self):
        while self != None:
            print(self.data)
            self = self.prev
        

arr = [1,2,3,4,5,6]
head = DoublyLinkedList(arr[0])
temp = head
for i in range(1, len(arr)):
    node = DoublyLinkedList(arr[i])
    temp.next = node
    node.prev = temp
    temp = temp.next
    if i == len(arr)-1:
        tail = temp

head.print_forward()
print('\n')
tail.print_back()
