class TreeNode:

    root = None

    def __init__(self, data) -> None:
        self.left = None
        self.right = None
        self.data = data


def createTree():
    first = TreeNode(1)
    second = TreeNode(2)
    third = TreeNode(3)
    fourth = TreeNode(4)
    fifth = TreeNode(5)
    sixth = TreeNode(6)
    seventh = TreeNode(7)

    TreeNode.root = first # 2<--1-->3     4<--2-->5    6<--3-->7
    first.left = second
    first.right = third
    second.left = fourth
    second.right = fifth
    third.left = sixth
    third.right = seventh

    









