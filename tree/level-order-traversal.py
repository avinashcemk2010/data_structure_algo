from collections import deque
from binary_tree import *

def level_order_traversal(root):
    if root is None:
        return

    # Initialize a queue
    queue = deque([root])

    # Loop until the queue is empty
    while queue:
        # Dequeue a node from the front
        node = queue.popleft()
        print(node.data, end=' ')

        # Enqueue left child
        if node.left:
            queue.append(node.left)

        # Enqueue right child
        if node.right:
            queue.append(node.right)


createTree()
level_order_traversal(TreeNode.root)
print()