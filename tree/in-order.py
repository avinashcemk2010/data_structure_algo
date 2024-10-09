from binary_tree import *
from collections import deque

def pre_order(root):
    if root == None:
        return

    pre_order(root.left)
    print(root.data, end="-->")
    pre_order(root.right) 

def pre_order_loop(root):
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
pre_order(TreeNode.root)
print()

pre_order_loop(TreeNode.root)