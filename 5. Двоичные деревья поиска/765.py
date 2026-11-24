import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.count = 1
        self.left = None
        self.right = None

def insert(root, key):
    if root is None: return Node(key)
    if key == root.key:
        root.count += 1
        return root
    elif key < root.key: 
        root.left = insert(root.left, key)
    else: 
        root.right = insert(root.right, key)
    return root

def print_freq(root):
    if root:
        print_freq(root.left)
        print(f"{root.key} {root.count}")
        print_freq(root.right)

if __name__ == "__main__":
    nums = [int(x) for x in sys.stdin.read().split()]
    root = None
    for x in nums:
        if x == 0: break
        root = insert(root, x)
    print_freq(root)
