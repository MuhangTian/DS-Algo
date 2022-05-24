class TreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def insert(self, val):
        # Case for inserting the 1st node
        if self.data == None:
            self.data = val
            return
        # Cannot allow duplicates
        if val == self.data:
            return
        if val < self.data:
            # NOTE: we can't use self==None at top since None does not have insert() as its method
            # sow we check it using if instead
            if self.left == None:
                self.left = TreeNode(val)
            else:
                self.left.insert(val)       
        if val > self.data:
            if self.right == None:
                self.right = TreeNode(val)
            else: 
                self.right.insert(val)
    
    def traverse(self, arr):
        if self.left == None and self.right == None:
            arr.append(self.data)
            return arr
        if self.left != None:
            self.left.traverse(arr)
            
        arr.append(self.data)
        
        if self.right != None:
            self.right.traverse(arr)
        
        return arr

    def get_successor(self, successor):
        if self.left != None:
            self.left = self.left.get_successor(successor)
            return self
        else:
            successor.data = self.data
            if self.right == None:
                return None
            else:
                return self.right
        
    def delete(self, val):
        # NOTE: 1.if no child, just remove
        # 2.if there is one child, delete node, place child at original position
        # 3.if there are two children, switch with least value that is greater
        # equivalent to the bottom child of the right child of the node to be deleted
        # (This is namely a successor node. Greatest value that is smaller can also work)
        # 4. if successor node also has a right child, replace successor node with it
        # 5. if value doesn't exist in tree, raise exception
        
        # NOTE: the key in deletion for node structure is to manipulate pointers, not to set
        # node = None, this is because Python passes parameter as a copy of original reference
        
        if val == self.data:
            if self.left == None:
                return self.right
            elif self.right == None:
                return self.left
            else:
                successor = TreeNode()
                self.right = self.right.get_successor(successor)
                self.data = successor.data
                return self
        
        if val < self.data:
            if self.left != None:
                self.left = self.left.delete(val)
                return self
            else:
                raise Exception("Value Not Found")
        elif val > self.data:
            if self.right != None:
                self.right = self.right.delete(val)
                return self
            else:
                raise Exception("Value Not Found")
        
    def search(self, val):
        if val == self.data:
            return val
        if val < self.data:
            if self.left != None:
                return self.left.search(val)
            else:
                raise Exception("Value Not Found")
            
        if val > self.data:
            if self.right != None:
                return self.right.search(val)
            else:
                raise Exception("Value Not Found")
        
        
        
        
arr = [4,8,6,9,3,1,7]
one = []
two = []
root = TreeNode()
for val in arr:
    root.insert(val)
print(root.traverse(one))
root.delete(4)
print(root.traverse(two)) 
print(root.search(6))    