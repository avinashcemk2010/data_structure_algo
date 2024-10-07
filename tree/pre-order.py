from binary_tree import *
from collections import deque

def pre_order_recursion(root):
    if root == None:
        return

    print(root.data, end="-->")

    pre_order_recursion(root.left)
    pre_order_recursion(root.right) 


def pre_order_loop(root):
    # use deque as stack
    stack = deque()

    if root == None:
        return

    stack.append(root)

    while len(stack) > 0:
        temp = stack.pop()
        print(temp.data, end="-->")

        if temp.right != None:
            stack.append(temp.right)
        if temp.left != None:
            stack.append(temp.left) 


createTree()
pre_order_recursion(TreeNode.root)
print()
pre_order_loop(TreeNode.root)