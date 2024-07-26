class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def find_min_value(node):
    current = node
    # Проходимо до найлівішого вузла
    while current.left is not None:
        current = current.left
    return current.val

root = TreeNode(40)
root.left = TreeNode(30)
root.right = TreeNode(80)
root.left.left = TreeNode(20)
root.left.right = TreeNode(50)
root.right.left = TreeNode(70)
root.right.right = TreeNode(90)

print(find_min_value(root))