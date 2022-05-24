class LinkedList:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
    
    def print(self):
        while self != None:
            print(self.data)
            self = self.next
        
def insert(arr):
    head = LinkedList(arr[0])
    temp = head
    for i in range(1, len(arr)):
        temp.next = LinkedList(arr[i])
        temp = temp.next
    return head

arr = [1,2,3,4,5,6]
head = insert(arr)
head.print()   