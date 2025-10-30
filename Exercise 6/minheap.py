class MinHeap:
    def __init__(self, A: list):
        self.heap = A.copy()
        n = len(self.heap)
        for i in range(n // 2 - 1, -1, -1):
            self.heap_down(i)
    
    def heap_down(self, i):
        n = len(self.heap)
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right
        
        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self.heap_down(smallest)
    
    def heap_up(self, i):
        parent = (i - 1) // 2
        if i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            self.heap_up(parent)
    
    def print(self):
        print(' '.join(map(str, self.heap)))
    
    def push(self, key: int):
        self.heap.append(key)
        self.heap_up(len(self.heap) - 1)
    
    def pop(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        min_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heap_down(0)
        
        return min_val


if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()  # 1 4 2 5 8 6 3
    print(heap.pop())  # 1
    heap.push(9)
    heap.print()  # 2 4 3 5 8 6 9