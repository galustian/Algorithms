class MinHeap:
    def __init__(self, criterion='w'):
        self.cr = criterion
        self.heap = [None]
    
    def is_empty(self): return len(self.heap) == 1

    def getMin(self):
        min_ = self.heap[1]
        
        self.heap[1] = self.heap[-1]
        del self.heap[-1]

        self.top_down_heapify()
        return min_
    
    # criterion must be accesible with item[criterion]
    def insert(self, item):
        self.heap.append(item)
        self.bottom_up_heapify()

    def bottom_up_heapify(self):
        i, cr = len(self.heap)-1, self.cr
        while i > 1 and self.heap[i//2][cr] > self.heap[i][cr]:
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i //= 2
    
    def top_down_heapify(self):
        i, cr = 1, self.cr
        while i*2 <= len(self.heap)-1:
            j = i*2
            if j < len(self.heap)-1 and self.heap[j][cr] > self.heap[j+1][cr]: j += 1
            if self.heap[i][cr] <= self.heap[j][cr]: break
            
            self.heap[j], self.heap[i] = self.heap[i], self.heap[j]
            i = j
