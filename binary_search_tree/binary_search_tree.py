"""
Binary search trees are a data structure that enforce an ordering over 
the data they store. That ordering in turn makes it a lot more efficient 
at searching for a particular piece of data in the tree. 

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
import sys
sys.path.append('queue/')
from queue import Queue
class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        if value < self.value:
            if not self.left:
                self.left = BSTNode(value)
            else:
                self.left.insert(value)
        else:
            if not self.right:
                self.right = BSTNode(value)
            else:
                self.right.insert(value)
            

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        if self.value == target:
            return True

        if target < self.value:
            if not self.left:
                return False
            else:
                return self.left.contains(target)
        else:
            if not self.right:
                return False    
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # recursive way
        if not self.right:
            return self.value
        return self.right.get_max()

        # iterative way
        # max_value = self.value

        # current_node = self

        # while current_node:
        #     if current_node.value > max_value:
        #         max_value = current_node.value
        #     current_node = current_node.right
        # return max_value

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        fn(self.value)

        if self.left:
            self.left.for_each(fn)

        if self.right:
            self.right.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self):
        if self.value:
            if self.left:
                self.left.in_order_print()
            print(self.value)
            if self.right:
                self.right.in_order_print()
        
    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self):
        q = Queue()
        visited = []
        # print(dir(q))
        
        def rec(tree):
            if tree.value not in visited:
                q.enqueue(tree.value)
                visited.append(tree.value)
            if tree.left:
                q.enqueue(tree.left.value)
                visited.append(tree.left.value)
            if tree.right:
                q.enqueue(tree.right.value)
                visited.append(tree.right.value)
            if tree.left:
                rec(tree.left)
            if tree.right:
                rec(tree.right)
        rec(self)

        string = ''
        for x in range(q.__len__()):
            
            string += f'{q.dequeue()}\n'
            # print(value)
        
        print(string)
        return string
        pass
        

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self):
        pass

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    def pre_order_dft(self):
        pass

    # Print Post-order recursive DFT
    def post_order_dft(self):
        pass

"""
This code is necessary for testing the `print` methods
"""
bst = BSTNode(1)

bst.insert(8)
bst.insert(5)
bst.insert(7)
bst.insert(6)
bst.insert(3)
bst.insert(4)
bst.insert(2)

# bst.in_order_print()
bst.bft_print()
# bst.dft_print()

# print("elegant methods")
# print("pre order")
# bst.pre_order_dft()
# print("in order")
# bst.in_order_dft()
# print("post order")
# bst.post_order_dft()  

# test = Queue()
# print(test.__len__())
# print(test.enqueue(1))
# print(test.__len__())