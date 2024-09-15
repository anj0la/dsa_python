def selection_sort(arr: list) -> None:
    """
    Implements the selection sort algorithm.

    Args:
        arr (list): The input array.
    """
    n = len(arr)
    for j in range(n):
        i_min = j
        # Find the minimum element in the unsorted array
        for i in range(j + 1, n):
            if arr[i] < arr[i_min]:
                i_min = i
        if i_min != j:
            arr[i_min], arr[j] = arr[j], arr[i_min]
            
            
def stable_selection_sort(arr: list) -> None:
    """
    Implements the selection sort algorithm, modified to be stable.

    Args:
        arr (list): The input array.
    """
    n = len(arr)
    for j in range(n):
        # Find the minimum element in the unsorted array
        i_min = j
        for i in range(j + 1, n):
            if arr[i] < arr[i_min]:
                i_min = i
                
        # Instead of swapping, insert the minimum element in its correct position in the original array
        value = arr[i_min]
        while i_min > j:
            arr[i_min] = arr[i_min - 1]
            i_min -= 1
            
        arr[j] = value
        