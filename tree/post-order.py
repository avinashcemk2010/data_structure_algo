from binary_tree import *
from collections import deque

def post_order_recursion(root):
    if root == None:
        return

    post_order_recursion(root.left)
    post_order_recursion(root.right) 
    print(root.data, end="-->")


def post_order_iterative(root):
    if root is None:
        return

    # Create two stacks
    stack1 = []
    stack2 = []

    # Push the root to the first stack
    stack1.append(root)

    # Run while the first stack is not empty
    while stack1:
        # Pop an item from stack1 and push it to stack2
        node = stack1.pop()
        stack2.append(node)

        # Push the left and right children of the popped node to stack1
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)

    # The elements in stack2 are in postorder, so print them
    while stack2:
        node = stack2.pop()
        print(node.data, end='-->')


createTree()
post_order_recursion(TreeNode.root)
print()
post_order_iterative(TreeNode.root)


