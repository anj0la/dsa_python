from data_structures.binary_heap import MaxHeap

def heap_sort(arr: list[int]) -> None:
    """
    Implements the heapsort algorithm.

    Args:
        arr (list[int]): The input array.
    """
    max_heap = MaxHeap()
    max_heap.build_max_heap(arr)
    heap_size = len(max_heap.heap)
    
    for i in range(heap_size - 1, 0, -1):
        # Swap the first element (max) with the last element
        max_heap.heap[0], max_heap.heap[i] = max_heap.heap[i], max_heap.heap[0]
        # Reduce the size of the heap and restore the heap property for the unsorted portion
        max_heap.heapify(0, i)
    # Copy the sorted elements back into the input array
    arr = max_heap.heap