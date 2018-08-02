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
            self.inOrder(treeNode.left):
            print(treeNode.data)
            self.inOrder(treeNode.right)

    def preOrder(self, treeNode=None):
        if treeNode:
            print(treeNode.data)
            self.preOrder(treeNode.left)
            self.preOrder(treeNode.right)

    def postOrder(self, treeNode=None):
        if treeNode:
            self.postOrder(treeNode.left)
            self.postOrder(treeNode.right)
            print(treeNode.data)

    def successor(self, treeNode):
        if treeNode.right:
            return self.min(treeNode.right)
        
        current = treeNode.parent
        while current and current.right == treeNode:
            treeNode = current
            current = current.parent
        return current

    

