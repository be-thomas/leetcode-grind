class Heap:
    def __init__(self, arr):
        # Initialize heap with None at index 0 since we want heap to start from index 1
        # This makes parent-child relationships easier to calculate
        # FIXME: As of now we assume this array is already a valid heap
        self.heap = [None] + arr

    def push(self, value):
        # Add the new value at the end of the heap
        self.heap.append(value)

        def bubble_up(index):
            # Base case: if we're at root (index 1), stop
            if index == 1:
                return

            # Calculate parent index
            parent_index = index // 2

            # If parent is greater than current element, swap them
            if self.heap[parent_index] > self.heap[index]:
                # Swap the elements
                self.heap[parent_index], self.heap[index] = (
                    self.heap[index],
                    self.heap[parent_index],
                )
                # Recursively bubble up from the parent position
                bubble_up(parent_index)

        # Start bubbling up from the last inserted element
        bubble_up(len(self.heap) - 1)

        # Print heap state after insertion (for debugging)
        print(f"Heap after inserting {value}: {self.heap}")

    def pop(self):
        res = self.heap[1]
        # Now we need to move the last element to the root and bubble it down
        self.heap[1] = self.heap[-1]
        self.heap.pop()

        def bubble_down(index):
            left_index = index * 2
            right_index = index * 2 + 1
            smallest_index = index

            # Check if left child exists and is smaller than current
            if (
                left_index < len(self.heap)
                and self.heap[left_index] < self.heap[smallest_index]
            ):
                smallest_index = left_index

            # Check if right child exists and is smaller than current smallest
            if (
                right_index < len(self.heap)
                and self.heap[right_index] < self.heap[smallest_index]
            ):
                smallest_index = right_index

            # If the smallest is not the current index, swap and continue bubbling down
            if smallest_index != index:
                self.heap[index], self.heap[smallest_index] = (
                    self.heap[smallest_index],
                    self.heap[index],
                )
                bubble_down(smallest_index)

        return res


heap = Heap([9, 10, 15, 20, 22, 23])
heap.insert(6)
