from node import Node


class BST:
    def __init__(self):
        self.size = 0
        self.root = None

    def __len__(self):
        return self.size

    def empty(self):
        return self.root is None

    def search(self, node, data):
        if not node or node.data == data:
            return node

        if node.data > data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def in_order(self, node=None):
        if node:
            self.in_order(node.left)
            print(node.data, end=" ")
            self.in_order(node.right)

    def pre_order(self, node=None):
        if node:
            print(node.data, end=" ")
            self.pre_order(node.left)
            self.pre_order(node.right)

    def post_order(self, node=None):
        if node:
            self.post_order(node.left)
            self.post_order(node.right)
            print(node.data, end=" ")

    def successor(self, node):
        if node.right:
            return self.min(node.right)

        current = node.parent
        while current and current.right == node:
            node = current
            current = current.parent
        return current

    """
    A new key is always inserted at leaf. We start searching a key from root
    till we hit a leaf node. Once a leaf node is found, the new node is added
    as a child of the leaf node.
    """
    def insert(self, data):
        parent = None
        new_node = Node(data)
        current = self.root

        while current:
            parent = current
            if current.data > new_node.data:
                current = current.left
            else:
                current = current.right

        new_node.parent = parent
        if parent is None:
            self.root = new_node    # tree empty
        elif parent.data > new_node.data:
            parent.left = new_node
        else:
            parent.right = new_node

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
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                mini = self.successor(root)
                root.data = mini.data
                root.right = self.delete(root.right, mini.data)
        return root

    @staticmethod
    def min(node):
        while node.left:
            node = node.left
        return node

    @staticmethod
    def max(node):
        while node.right:
            node = node.right
        return node

    @staticmethod
    def search_iterative(node, data):
        while node and node.data != data:
            if node.data > data:
                node = node.left
            else:
                node = node.right
        return node

    @staticmethod
    def in_order_iterative(node):
        current, stack = node, []

        while current or stack:
            while current:
                stack.append(current)
                current = current.left

            current = stack.pop()
            print(current.data, end=" ")
            current = current.right

    @staticmethod
    def pre_order_iterative(node):
        stack = [node]
        while stack:
            current = stack.pop()
            print(current.data, end=" ")
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)

    @staticmethod
    def post_order_iterative(node):
        current, items = [node], []

        while current:
            node = current.pop()
            items.append(node)

            if node.left:
                current.append(node.left)
            if node.right:
                current.append(node.right)

        while items:
            current = items.pop()
            print(current.data, end=" ")

