"""
Assessment 3.6: DFS Methods in Tree
Name: Lanz Casinao

This program builds a binary tree using the letters in the first name
LANZ followed by the last name CASINAO. The letters are inserted in
level-order (left to right, one level at a time), matching Assessment 3.5.

It then displays the three Depth-First Search (DFS) traversals:
1. Preorder  - Root, Left, Right
2. Inorder   - Left, Root, Right
3. Postorder - Left, Right, Root
"""

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def build_complete_binary_tree(values):
    """Build a binary tree by placing values level by level."""
    if not values:
        return None

    nodes = [Node(value) for value in values]

    for index in range(len(nodes)):
        left_index = 2 * index + 1
        right_index = 2 * index + 2

        if left_index < len(nodes):
            nodes[index].left = nodes[left_index]

        if right_index < len(nodes):
            nodes[index].right = nodes[right_index]

    return nodes[0]


def preorder(root, result):
    """Visit Root -> Left -> Right."""
    if root is not None:
        result.append(root.data)
        preorder(root.left, result)
        preorder(root.right, result)


def inorder(root, result):
    """Visit Left -> Root -> Right."""
    if root is not None:
        inorder(root.left, result)
        result.append(root.data)
        inorder(root.right, result)


def postorder(root, result):
    """Visit Left -> Right -> Root."""
    if root is not None:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.data)


def main():
    name_letters = list("LANZCASINAO")
    root = build_complete_binary_tree(name_letters)

    pre_result = []
    in_result = []
    post_result = []

    preorder(root, pre_result)
    inorder(root, in_result)
    postorder(root, post_result)

    print("=" * 50)
    print("ASSESSMENT 3.6: DFS METHODS IN TREE")
    print("Name: Lanz Casinao")
    print("Letters used:", " ".join(name_letters))
    print("=" * 50)

    print("\nBinary Tree (level-order arrangement):")
    print("                 L")
    print("              /     \\")
    print("             A       N")
    print("           /   \\   /   \\")
    print("          Z     C A     S")
    print("         / \\   / \\ /")
    print("        I   N A   O")

    print("\nDFS TRAVERSALS")
    print("Preorder  (Root -> Left -> Right):")
    print(" -> ".join(pre_result))

    print("\nInorder   (Left -> Root -> Right):")
    print(" -> ".join(in_result))

    print("\nPostorder (Left -> Right -> Root):")
    print(" -> ".join(post_result))


if __name__ == "__main__":
    main()
