class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def is_valid_bst(node, left=float('-inf'), right=float('inf')):
    # Base case: if the node is None, it's valid (an empty tree is a valid BST)
    if not node:
        return True
    
    # The current node's value must be between the left and right bounds
    if not (left < node.val < right):
        return False
    
    # Recursively validate the left and right subtrees with updated bounds
    return (is_valid_bst(node.left, left, node.val) and
            is_valid_bst(node.right, node.val, right))

# Example usage
# Create a binary tree: 
#        5
#       / \
#      3   8
#     / \   \
#    2   4   10
root = TreeNode(5)
root.left = TreeNode(3)
root.right = TreeNode(8)
root.left.left = TreeNode(2)
root.left.right = TreeNode(4)
root.right.right = TreeNode(10)

# Validate if the binary tree is a valid BST
print(is_valid_bst(root))  # Output: True
