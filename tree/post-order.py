from binary_tree import *
from collections import deque

def post_order_recursion(root):
    if root == None:
        return

    post_order_recursion(root.left)
    post_order_recursion(root.right) 
    print(root.data, end="-->")


createTree()
post_order_recursion(TreeNode.root)


