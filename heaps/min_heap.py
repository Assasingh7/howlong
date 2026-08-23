class MinHeap:

    def __init__(self):
        self.heap = []

    def insert(self, value):

        # Add at the end
        self.heap.append(value)

        # Index of new element
        i = len(self.heap) - 1

        # Heapify up
        while i > 0:

            parent = (i - 1) // 2

            # Already in correct position
            if self.heap[parent] <= self.heap[i]:
                break

            # Swap with parent
            self.heap[parent], self.heap[i] = \
                self.heap[i], self.heap[parent]

            # Move upward
            i = parent

    def deleteMin(self):

        # Heap is empty
        if not self.heap:
            return None

        # Save minimum
        minimum = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap[-1]

        # Remove last element
        self.heap.pop()

        # Heapify down
        i = 0
        n = len(self.heap)

        while True:

            left = 2 * i + 1
            right = 2 * i + 2

            # Assume current is smallest
            smallest = i

            # Check left child
            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            # Check right child
            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            # Current is already smallest
            if smallest == i:
                break

            # Swap with smaller child
            self.heap[i], self.heap[smallest] = \
                self.heap[smallest], self.heap[i]

            # Move downward
            i = smallest

        return minimum