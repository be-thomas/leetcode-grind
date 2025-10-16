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


heap = Heap([9, 10, 15, 20, 22, 23])
heap.insert(6)
