def insertion_sort(arr: list) -> None:
    """
    Implements the insertion sort algorithm.

    Args:
        arr (list): The input array.
    """
    n = len(arr)
    for i in range(1, n):
        j = i
        while j > 0 and arr[j - 1] > arr[j]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j -= 1