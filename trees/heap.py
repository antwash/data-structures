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

    def insert(self, value):
        index = self.heapSize
        if index == len(self.values):
            self.values.append(value)
        else:
            self.values[index] = value
        self.heapSize += 1
        self.heapify_up(index)

    def delete(self, value):
        v = self.values
        if value in v:
            index = v.index(value)
            last = self.heapSize - 1
            v[index], v[last] = v[last], None
            self.heapSize -= 1
            self.heapify_down(index)
        else:
            print("Value doesn't exist in the heap.")

    def heapify_up(self, index):
        parent = self.parent(index)
        if parent >= 0:
            v = self.values 
            if v[parent] < v[index]:
                v[parent], v[index] = v[index], v[parent]
                self.heapify_up(parent)

    def heapify_down(self, index):
        v = self.values
        largest = index
        last = self.heapSize - 1
        
        left = self.left_child(index)
        right = self.right_child(index)

        if left <= last and v[left] > v[largest]:
            largest = left
        if right <= last and v[right] > v[largest]:
            largest = right

        if largest != index:
            v[largest], v[index] = v[index], v[largest]
            self.heapify_down(largest)

    @staticmethod
    def parent(index):
        return int((index - 1) / 2)

    @staticmethod
    def left_child(index):
        return 2 * index + 1

    @staticmethod
    def right_child(index):
        return 2 * index + 2
