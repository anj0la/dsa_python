def selection_sort(arr: int) -> None:
    """
    Implements the selection sort algorithm.

    Args:
        arr (list): The input array.
    """
    n = len(arr)
    for j in range(n):
        i_min = j
        for i in range(j + 1, n):
            if arr[i] < arr[i_min]:
                i_min = i
        if i_min != j:
            arr[i_min], arr[j] = arr[j], arr[i_min]