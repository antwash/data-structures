"""   
    Implementation that would build a heap from a list
    but the list are passed by copy instead of reference.

    def max_heapify(self, v):
        if v:
            n = int(len(v) / 2) - 1
            for index in range(n, 0, -1):
                self.heapifyDown(index, values=v)
        print("Heaped built from values: ~>", v)
""" 

class Heap:
    def __init__(self):
        self.values = []
        self.heapSize = 0

    def parent(self, index):
        return int((index - 1) / 2)

    def leftChild(self, index):
        return 2 * index + 1

    def rightChild(self, index):
        return 2 * index + 2

    def insert(self, value):
        index = self.heapSize
        if index == len(self.values):
            self.values.append(value)
        else:
            self.values[index] = value
        self.heapSize += 1
        self.heapifyUp(index)

    def delete(self, value):
        v = self.values
        if value in v:
            index = v.index(value)
            last = self.heapSize - 1
            v[index], v[last] = v[last], None
            self.heapSize -= 1
            self.heapifyDown(index)
        else:
            print("Value doesn't exist in the heap.")

    def heapifyUp(self, index):
        parent = self.parent(index)
        if parent >= 0:
            v = self.values 
            if v[parent] < v[index]:
                v[parent], v[index] = v[index], v[parent]
                self.heapifyUp(parent)

    def heapifyDown(self, index):
        v = self.values
        largest = index
        last = self.heapSize - 1
        
        left = self.leftChild(index)
        right = self.rightChild(index)

        if left <= last and v[left] > v[largest]:
            largest = left
        if right <= last and v[right] > v[largest]:
            largest = right

        if largest != index:
            v[largest], v[index] = v[index], v[largest]
            self.heapifyDown(largest)
