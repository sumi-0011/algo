class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = self.right = None


class BinaryTree(object):
    def __init__(self):
        self.root = None

    def preorder(self):  # 전위 순회
        # left 부터
        def _preorder(node):
            print(node.item, end="")
            if node.left:
                _preorder(node.left)
            if node.right:
                _preorder(node.right)

        _preorder(self.root)

    def midorder(self):  # 중위 순회
        def _midorder(node):
            if node.left:
                _midorder(node.left)
            print(node.item, end="")
            if node.right:
                _midorder(node.right)

        _midorder(self.root)

    def afterorder(self):  # 중위 순회
        def _afterorder(node):
            if node.left:
                _afterorder(node.left)
            if node.right:
                _afterorder(node.right)
            print(node.item, end="")

        _afterorder(self.root)


import sys


def node_init(N):
    node_dict = {'.': None}
    for x in range(N):
        al = chr(ord('A') + x)
        node_dict[al] = Node(al)

    return node_dict


if __name__ == "__main__":
    N = int(sys.stdin.readline().strip())

    node_dict = node_init(N)
    BT = BinaryTree()
    BT.root = node_dict['A']

    for _ in range(N):
        ro, l, r = map(str, sys.stdin.readline().split())
        ro_node, l_node, r_node = node_dict[ro], node_dict[l], node_dict[r]
        ro_node.left = l_node
        ro_node.right = r_node

    BT.preorder()
    print()
    BT.midorder()
    print()
    BT.afterorder()
