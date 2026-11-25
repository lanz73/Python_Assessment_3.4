from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def insert(root, value):
    if root is None:
        return Node(value)
    if value < root.value:
        root.left = insert(root.left, value)
    elif value > root.value:
        root.right = insert(root.right, value)
    return root

def bfs(root):
    if root is None:
        return []
    result, queue = [], deque([root])
    while queue:
        node = queue.popleft()
        result.append(node.value)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return result

def dfs_preorder(root):
    if root is None:
        return []
    return [root.value] + dfs_preorder(root.left) + dfs_preorder(root.right)

def print_tree(root, level=0, label="Root"):
    if root:
        print("    " * level + f"{label}: {root.value}")
        print_tree(root.left, level + 1, "Left")
        print_tree(root.right, level + 1, "Right")

if __name__ == "__main__":
    root = None
    for letter in "CASINAO":
        root = insert(root, letter)
    print("BINARY SEARCH TREE - CASINAO")
    print_tree(root)
    print("\nBFS:", " - ".join(bfs(root)))
    print("DFS (Preorder):", " - ".join(dfs_preorder(root)))
