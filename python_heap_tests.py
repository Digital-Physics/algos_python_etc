print("heaps are one instance of a 'priority queue'")
print("heaps are good for getting the min or max of a list")
print("that process of getting a min or max can be done in log time, not linear time like with a normal list")
print("A heap is a tree but it's organized in a list, not using tree/node class objects with children")
print("A heap is quicker to set up (O(n)) than making a BST (O(n*log(n)))")
print("You can actually use a heap to create a sorted list in (O(n*log(n)))")


class MinHeap:
    def __init__(self, array):
        self.heap = array
        self.build_heap(array)

    # time: O(n) constructing a min heap and removing the min is quicker than sorting and having BST retrieval
    # space: O(1) swaps of elements in array/heap done in place
    def build_heap(self, array):
        # use sift_down over sift_up since it is faster for majority of nodes (towards bottom)
        # you don't need to sift_down any leaf nodes so just start with the last parent in heap/tree
        # heap index property: min is 0 index, then l_idx = curr_idx * 2 + 1 and r_idx = curr_idx * 2 + 2
        last_parent_idx = ((len(array)-1)-1)//2
        for curr_idx in reversed(range(last_parent_idx + 1)):  # +1 to include it in range
            self.sift_down(curr_idx)

    # time: O(log(n))
    # space: O(1)
    def sift_down(self, curr_idx):
        l_idx = curr_idx * 2 + 1

        while l_idx <= len(self.heap) - 1:
            r_idx = curr_idx * 2 + 2
            if r_idx > len(self.heap) - 1:
                r_idx = None

            if r_idx is not None and self.heap[r_idx] < self.heap[l_idx]:
                potential_swap = r_idx
            else:
                potential_swap = l_idx

            if self.heap[potential_swap] < self.heap[curr_idx]:
                self.heap[potential_swap], self.heap[curr_idx] = self.heap[curr_idx], self.heap[potential_swap]
                potential_swap, curr_idx = curr_idx, potential_swap
                l_idx = curr_idx * 2 + 1
            else:
                break

    # time: O(log(n))
    # space: O(1)
    def sift_up(self, curr_idx):  # (in a min heap)
        parent_idx = (curr_idx - 1) // 2
        # do iterative instead of recursion
        while curr_idx > 0 and self.heap[parent_idx] > self.heap[curr_idx]:
            self.heap[parent_idx], self.heap[curr_idx] = self.heap[curr_idx], self.heap[parent_idx]
            curr_idx = parent_idx
            parent_idx = (curr_idx - 1) // 2

    # time: O(1)
    # space: O(1)
    def peek(self):
        return self.heap[0]

    # time: O(log(n))
    # space: O(1)
    def remove(self):  # (the top of the heap) (and return it)
        # (since heap not sorted, it is not meant for quick removal of other values)
        # swap first/top and last and then remove last(which was top) before sift_down on temp top
        self.heap[0], self.heap[len(self.heap) - 1] = self.heap[len(self.heap) - 1], self.heap[0]
        removed_value = self.heap.pop()
        self.sift_down(0)
        return removed_value

    # time: O(log(n))
    # space: O(1)
    def insert(self, value):
        # add val to the end of the heap tree, and then sift it up into place
        self.heap.append(value)
        self.sift_up(len(self.heap) - 1)


h = MinHeap([1, 8, -2, 8, 9, 3, 4])
print(h.heap)

print("heap property: each parent is less than (in the case of MinHeap) (or equal to) its children")
#      -2
#   8       1
# 8   9   3   4

h.insert(-3)
print(h.heap)

print(h.remove())
print(h.remove())
print(h.heap)

#      1
#   8       3
# 8   9   4
