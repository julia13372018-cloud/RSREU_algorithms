import sys

class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        print("DONE")
        return Node(key)
    if key == root.key:
        print("ALREADY")
        return root
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def search(root, key):
    if root is None:
        return False
    if root.key == key:
        return True
    if key < root.key:
        return search(root.left, key)
    return search(root.right, key)

def delete(root, key):
    if root is None:
        print("CANNOT")
        return None
    if key < root.key:
        root.left = delete(root.left, key)
    elif key > root.key:
        root.right = delete(root.right, key)
    else:
        print("DONE")
        if root.left is None: return root.right
        if root.right is None: return root.left
    return root

def print_tree(root, level=0):
    if root is None:
        return
    print_tree(root.left, level + 1)
    print("." * level + str(root.key))
    print_tree(root.right, level + 1)

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()
    root = None
    for line in lines:
        if not line: continue
        parts = line.split()
        cmd = parts[0]
        if cmd == "ADD":
            root = insert(root, int(parts[1]))
        elif cmd == "SEARCH":
            print("YES" if search(root, int(parts[1])) else "NO")
