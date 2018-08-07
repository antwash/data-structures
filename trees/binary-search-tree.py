class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    def empty(self):
        return self.root == None

    def min(self, treeNode):
        while treeNode.left:
            treeNode = treeNode.left
        return treeNode

    def max(self, treeNode):
        while treeNode.right:
            treeNode = treeNode.right
        return treeNode

    def search(self, treeNode, data):
        if not treeNode or treeNode.data == data:
            return treeNode

        if treeNode.data > data:
           return self.search(treeNode.left, data)
        else:
            return self.search(treeNode.right, data)

    def search_iterative(self, treeNode, data):
        while treeNode and treeNode.data != data:
            if treeNode.data > data:
                treeNode = treeNode.left
            else:
                treeNode = treeNode.right
        return treeNode

    def inOrder(self, treeNode=None):
        if treeNode:
            self.inOrder(treeNode.left)
            print(treeNode.data, end=" ")
            self.inOrder(treeNode.right)

    def preOrder(self, treeNode=None):
        if treeNode:
            print(treeNode.data, end=" ")
            self.preOrder(treeNode.left)
            self.preOrder(treeNode.right)

    def postOrder(self, treeNode=None):
        if treeNode:
            self.postOrder(treeNode.left)
            self.postOrder(treeNode.right)
            print(treeNode.data, end=" ")

    def bfs(self, treeNode):
        if not treeNode:
            return

        queue, visited = [treeNode], set()
        while queue:
            level = []
            for node in queue:
                if node not in visited:
                    visited.add(node)
                if node.left != None:
                    level.append(node.left)
                if node.right != None:
                    level.append(node.right)
            queue = level

    def successor(self, treeNode):
        if treeNode.right:
            return self.min(treeNode.right)

        current = treeNode.parent
        while current and current.right == treeNode:
            treeNode = current
            current = current.parent
        return current

    """
    A new key is always inserted at leaf. We start searching a key from root till we hit a leaf node. Once a leaf node is found, the new node is added as a child of the leaf node.
    """
    def insert(self, data):
        parent = None
        newNode = Node(data)
        current = self.root

        while current:
            parent = current
            if current.data > newNode.data:
                current = current.left
            else:
                current = current.right

        newNode.parent = parent
        if parent == None:
            self.root = newNode    # tree empty
        elif parent.data > newNode.data:
            parent.left = newNode
        else:
            parent.right = newNode

    def delete(self, root, data):
        if not root:
            return root
        elif root.data > data:  # match on left
            root.left = self.delete(root.left, data)
        elif root.data < data:  # match on right
            root.right = self.delete(root.right, data)
        else:
            """
            found match
            Case 1: No Children
            Case 2: One Child
            Case 3: Two Children
            """
            if root.left == None and root.right == None:
                return None
            elif root.left == None:
                return root.right
            elif root.right == None:
                return root.left
            else:
                mini = self.successor(root)
                root.data = mini.data
                root.right = self.delete(root.right, mini.data)
        return root
