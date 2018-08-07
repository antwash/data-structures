class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def __repr__(self):
        return str(self.data)

class SingleyLinkedList:
    def __init__(self, items=None):
        self.size = 0
        self.head = None
        if items:   
            for item in items: self.append(item)

    def __len__(self):
        return self.size

    def __repr__(self):
        curr, nodes = self.head, []
        while curr:
            nodes.append(str(curr))
            curr = curr.next
        return "~> ".join(nodes)
    
    def getFirst(self):
        return self.head

    def getLast(self):
        current = self.head
        while current.next:
            current = current.next
        return current

    def append(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1
    
    def remove(self, data):
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == data:
                found = True
            else:
                previous = current
                current = current.next
        
        if found:
            self.size -= 1
            if previous == None:
                self.head = self.head.next  # delete head 
            else:
                previous.next = current.next

    def contains(self, data):
        curr = self.head
        while curr and curr.data != data:
            curr = curr.next
        return curr
