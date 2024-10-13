from binary_tree import *

def findmax(root):
    if root == None:
        return float('-inf')

    result = root.data
    left = findmax(root.left)
    right = findmax(root.right)

    if left > result:
        result = left

    if right > result:
        result = right 

    return result

createTree()
print(findmax(TreeNode.root)) 