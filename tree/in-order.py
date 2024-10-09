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

createTree()
in_order(TreeNode.root)
print()

in_order_loop(TreeNode.root)