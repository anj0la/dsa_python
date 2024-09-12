def bubble_sort(arr: list) -> None:
    """
    Implements the bubble sort algorithm.

    Args:
        arr (list): The input array.
    """
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n - i - 1): # N - I elements have already been sorted
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def bubble_sort_optimized(arr: list) -> None:
    """
    Implements the bubble sort algorithm. 
   
    It is optimized by stopping the algorithm if no swaps occured in the inner loop (elements at that iteration are sorted).

    Args:
        arr (list): The input array.
    """
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # The elements are sorted, stop the algorithm  
        if not swapped:
            break

    