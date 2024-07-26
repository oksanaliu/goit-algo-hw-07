class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def sum_of_values(node):
    if node is None:
        return 0
    # Рекурсивно обходимо ліве і праве піддерево, додаючи значення вузлів
    return node.val + sum_of_values(node.left) + sum_of_values(node.right)

root = TreeNode(40)
root.left = TreeNode(30)
root.right = TreeNode(80)
root.left.left = TreeNode(20)
root.left.right = TreeNode(50)
root.right.left = TreeNode(70)
root.right.right = TreeNode(90)

print(sum_of_values(root))  