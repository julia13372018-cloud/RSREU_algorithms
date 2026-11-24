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

def find_second_max(root):
    curr = root
    parent = None
    while curr.right is not None:
        parent = curr
        curr = curr.right
    if curr.left is not None:
        curr = curr.left
        while curr.right is not None:
            curr = curr.right
        return curr.key
    return parent.key

if __name__ == "__main__":
    nums = [int(x) for x in sys.stdin.read().split()]
    root = None
    for x in nums:
        if x == 0: break
        root = insert(root, x)
    print(find_second_max(root))
