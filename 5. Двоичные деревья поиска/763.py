import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None: return Node(key)
    if key < root.key: root.left = insert(root.left, key)
    elif key > root.key: root.right = insert(root.right, key)
    return root

def print_branches(root):
    if root is None: return
    print_branches(root.left)
    if (root.left is None) != (root.right is None):
        print(root.key)
    print_branches(root.right)

if __name__ == "__main__":
    nums = [int(x) for x in sys.stdin.read().split()]
    root = None
    for x in nums:
        if x == 0: break
        root = insert(root, x)
    print_branches(root)
