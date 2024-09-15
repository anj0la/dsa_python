def merge(arr: list, low: int, mid: int, high: int):
    """
    Implements the merge function of the merge sort algorithm.

    Args:
        arr (list): The input array.
        low (int): The starting index of the first subarray.
        mid (int): The middle index, to divide the array into two subarrays.
        high (int): The ending index of the second subarray.
    """
    n1 = mid - low + 1
    n2 = high - mid
    
    left = [arr[low + i] for i in range(n1)]
    right = [arr[mid + 1 + j] for j in range(n2)]
    
    i = j = 0
    k = low
    
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1
            
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
        
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr: list, low: int, high: int) -> None:
    """
    Implements the merge sort algorithm.

    Args:
        arr (list): The input array.
        low (low): The starting index.
        high (_type_): The ending index.
    """
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)