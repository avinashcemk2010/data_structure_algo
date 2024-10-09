from binary_tree import *
from collections import deque

def in_order(root):
    if root == None:
        return

    in_order(root.left)
    print(root.data, end="-->")
    in_order(root.right) 

def in_order_loop(root):
    if root == None:
        return

    stack = deque()

    temp = root
    while len(stack) > 0 or temp != None:
        if temp != None:
            stack.append(temp)
            temp = temp.left
        else:
            temp = stack.pop()
            print(temp.data, end="-->")
            temp = temp.right

'''
Pseudocode for inorder traversal:
InorderTraversal(root):
    Initialize an empty stack
    current = root
    
    while current is not NULL or stack is not empty:
        while current is not NULL:
            stack.push(current)         # Push current node to the stack
            current = current.left      # Move to the left child
            
        current = stack.pop()            # Pop the top node
        Visit(current)                   # Visit the node (process or print)
        
        current = current.right          # Move to the right child

'''

def in_order_loop_2(root):
    current = root
    stack = deque()

    while current != None or len(stack) > 0:
        while current != None:
            stack.append(current)
            current = current.left

        current = stack.pop()
        print(current.data, end="-->")

        current = current.right



createTree()
in_order(TreeNode.root)
print()

in_order_loop(TreeNode.root)
print()

in_order_loop_2(TreeNode.root) 