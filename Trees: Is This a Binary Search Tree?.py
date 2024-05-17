""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""

def checkBST(root):
    def inorder_traversal(node, result):
        if node:
            inorder_traversal(node.left, result)
            result.append(node.data)
            inorder_traversal(node.right, result)

    # Perform inorder traversal to get the sequence of node values
    result = []
    inorder_traversal(root, result)

    # Check if the resulting sequence is sorted
    for i in range(1, len(result)):
        if result[i] <= result[i - 1]:
            return False

    return True
