from binary_tree import *

def pre_order(root):
    if root == None:
        return

    pre_order(root.left)
    print(root.data, end="-->")
    pre_order(root.right) 


def pre_order_loop():
    pass

createTree()
pre_order(TreeNode.root)
print()