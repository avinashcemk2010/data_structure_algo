from binary_tree import *
from collections import deque

def pre_order_recursion(root):
    if root == None:
        return

    print(root.data, end="-->")

    pre_order_recursion(root.left)
    pre_order_recursion(root.right) 


'''
Pseudocode for preorder traversal:
PreorderTraversal(root):
    if root is NULL:
        return
    
    Initialize an empty stack
    stack.push(root)
    
    while stack is not empty:
        current = stack.pop()
        Visit(current)                  # Visit the node (process or print)
        
        if current.right is not NULL:
            stack.push(current.right)   # Push the right child
        if current.left is not NULL:
            stack.push(current.left)    # Push the left child

'''

def pre_order_loop(root):
    # use deque as stack
    stack = deque()

    if root == None:
        return

    stack.append(root)

    while len(stack) > 0:
        current = stack.pop()
        print(current.data, end="-->")

        if current.right != None:
            stack.append(current.right)
        if current.left != None:
            stack.append(current.left) 


createTree()
pre_order_recursion(TreeNode.root)
print()
pre_order_loop(TreeNode.root)