# Binary heap tree implemented using array
class BinaryHeap:

    def __init__(self) -> None:
        self.data = []
    
    # Only insert at the back, similar to queue
    def insert(self, val, i=-1):
        # Case for the first call, since -1 is only possible for 1st call
        if i == -1:
            self.data.append(val)
            i = len(self.data)-1
        
        parent = int((i-1)/2)
        if self.data[parent] < self.data[i]:
            self.data[parent], self.data[i] = self.data[i], self.data[parent]
            return self.insert(val, parent)
        else:
            return
    
    # Only delete from the front, similar to queue
    def delete(self, i=-1):
        if i == -1:
            self.data[0] = self.data[len(self.data)-1]
            self.data.pop()
            i = 0
        
        lchild = 2*i+1
        rchild = 2*i+2
        if lchild and rchild <= len(self.data)-1:
            if self.data[rchild] > self.data[lchild]:
                self.data[rchild],self.data[i] = self.data[i], self.data[rchild]
                return self.delete(rchild)
            else:
                self.data[lchild],self.data[i] = self.data[i], self.data[lchild]
                return self.delete(lchild)
        else:
            return
    
    def read(self):
        return self.data[0]

arr = [1,87,4,9,2,6,10,17,143,57,29,1,6,2,6,100,25]
heap = BinaryHeap()
for val in arr:
    heap.insert(val)
print(heap.data)
heap.delete()
heap.delete()
heap.delete()
print(heap.data)
arr.sort()
arr.reverse()
print("Sorted original array: " + str(arr))


