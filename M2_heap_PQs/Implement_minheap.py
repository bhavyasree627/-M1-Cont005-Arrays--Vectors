class MinHeap:
    def __init__(self):
        self.heap = []

    def bubble_up(self, i):
        while i > 0:
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
                i = parent
            else:
                break

    def bubble_down(self, i):
        while 2 * i + 1 < len(self.heap):
            left_child = 2 * i + 1
            right_child = 2 * i + 2 if 2 * i + 2 < len(self.heap) else None
            min_child = left_child

            if right_child is not None and self.heap[right_child] < self.heap[left_child]:
                min_child = right_child

            if self.heap[i] > self.heap[min_child]:
                self.heap[i], self.heap[min_child] = self.heap[min_child], self.heap[i]
                i = min_child
            else:
                break

    def insert(self, num):
        self.heap.append(num)
        self.bubble_up(len(self.heap) - 1)

    def getMin(self):
        if not self.heap:
            return "Empty"
        else:
            return self.heap[0]

    def delMin(self):
        if not self.heap:
            return
        else:
            min_val = self.heap[0]
            self.heap[0] = self.heap[-1]
            self.heap.pop()
            self.bubble_down(0)
            return


# Main program
t = int(input())
min_heap = MinHeap()
for _ in range(t):
    operation = input().split()
    if operation[0] == "insert":
        min_heap.insert(int(operation[1]))
    elif operation[0] == "getMin":
        print(min_heap.getMin())
    elif operation[0] == "delMin":
        min_heap.delMin()
