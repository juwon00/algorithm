# 트리 부분 다시 공부할 필요
# 트리 만드는 방법, 순회 (전위, 후위, 중위, 레벨)

import sys

sys.setrecursionlimit(10 ** 6)


class Node:
    def __init__(self, val, index):
        self.val = val
        self.index = index
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val, index):
        self.root = self._insert(self.root, val, index)
        return self.root is not None

    def _insert(self, node, val, index):
        if node is None:
            return Node(val, index)

        if val < node.val:
            node.left = self._insert(node.left, val, index)
        else:
            node.right = self._insert(node.right, val, index)

        return node

    def preorder(self, n):
        if n != None:
            print(n.index, n.val, '', end='')  # 노드 방문
            preorderlist.append(n.index)
            if n.left: self.preorder(n.left)  # 왼쪽 서브트리 순회
            if n.right: self.preorder(n.right)  # 오른쪽 서브트리 순회

    def postorder(self, n):
        if n != None:
            if n.left: self.postorder(n.left)
            if n.right: self.postorder(n.right)
            print(n.index, n.val, '', end='')
            postorderlist.append(n.index)


preorderlist = []
postorderlist = []


def solution(nodeinfo):
    answer = []
    bst = BinaryTree()

    nodes = []
    for i, node in enumerate(nodeinfo):
        nodes.append([node, i + 1])
    nodes.sort(key=lambda x: (-x[0][1], x[0][0]))
    print(nodes)

    for node, index in nodes:
        print(node, index)
        bst.insert(node, index)

    bst.preorder(bst.root)
    print()
    bst.postorder(bst.root)
    print()
    print(preorderlist)
    print(postorderlist)

    answer.append(preorderlist)
    answer.append(postorderlist)

    return answer


nodeinfo = [[5, 3], [11, 5], [13, 3], [3, 5], [6, 1], [1, 3], [8, 6], [7, 2], [2, 2]]
answer = solution(nodeinfo)
print("answer:", answer)
