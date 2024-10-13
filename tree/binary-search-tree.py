# Define the structure of a node in the BST
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

# Function to insert a new node in the BST
def insert(root, key):
    # If the tree is empty, return a new node
    if root is None:
        return Node(key)

    # Otherwise, recur down the tree
    if key < root.val:
        root.left = insert(root.left, key)
    elif key > root.val:
        root.right = insert(root.right, key)

    # Return the (unchanged) node pointer
    return root

# Function for in-order traversal of the BST
# Inorder traversal in bst gives values in ascending order
def inorder(root):
    if root:
        # Traverse the left subtree
        inorder(root.left)
        # Print the value of the node
        print(root.val, end=' ')
        # Traverse the right subtree
        inorder(root.right)

# Example usage
if __name__ == "__main__":
    # Initialize an empty tree
    root = None

    # Insert nodes into the BST
    values = [20, 10, 30, 5, 15, 25, 35]
    for value in values:
        root = insert(root, value)

    # Perform in-order traversal
    print("In-order traversal of the BST:")
    inorder(root)
