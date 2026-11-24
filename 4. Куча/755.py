import sys

class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, k):
        self.heap.append(k)
        self.sift_up(len(self.heap) - 1)

    def sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] <= self.heap[parent]:
                break
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent

    def extract(self):
        if len(self.heap) == 1:
            return self.heap.pop()
        res = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.sift_down(0)
        return res

    def sift_down(self, i):
        n = len(self.heap)
        while 2 * i + 1 < n:
            left = 2 * i + 1
            right = 2 * i + 2
            j = left
            if right < n and self.heap[right] > self.heap[left]:
                j = right
            if self.heap[i] >= self.heap[j]:
                break
            self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
            i = j

if __name__ == "__main__":
    input_data = sys.stdin.read().split()
    if input_data:
        n = int(input_data[0])
        heap = MaxHeap()
        idx = 1
        for _ in range(n):
            cmd = input_data[idx]
            if cmd == '0':
                val = int(input_data[idx+1])
                heap.insert(val)
                idx += 2
            else:
                print(heap.extract())
                idx += 1
