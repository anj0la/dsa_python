def hoare_partition(arr: list, low: int, high: int) -> int:
    """
    Implements the Hoare partition with the pivot as the first element. 
    This partititoning scheme is the fastest out of three.

    Args:
        arr (list): The input array.
        low (int): The starting index of the subarray.
        high (int): The ending index of the subarray.

    Returns:
        int: The location of the pivot.
    """
    pivot = arr[low] # Selecting the first element as the pivot
    
    i = low - 1 # Left index
    j = high + 1 # Right index
    
    while True:
        
        # Find an element on the left-hand side that's greater than the pivot
        i += 1
        while arr[i] < pivot:
            i += 1
            
        # Find an element on the right hand-side that's smaller than the pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1
            
        # If the indices have crossed (left index >= right index), return the right index (j)
        if i >= j:
            return j # The pivot index
        
        arr[i], arr[j] = arr[j], arr[i]

def lomuto_partition(arr: list, low: int, high: int) -> int:
    """
    Implements the Lomuto partition with the pivot as the last element.

    Args:
        arr (list): The input array.
        low (int): The starting index of the subarray.
        high (int): The ending index of the subarray.

    Returns:
        int: The location of the pivot.
    """
    pivot = arr[high] # Selecting the last element as the pivot
    i = low - 1
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def naive_partition(arr: list, low: int, high: int) -> int:
    """
    Implements a naive partitioning by using a temporary array to store elements less than the pivot, the pivot itself, and elements greater than the pivot.
    The elements are copied over to the array, and the pivot location is returned.

    Args:
        arr (list): The input array.
        low (int): The starting index of the subarray.
        high (int): The ending index of the subarray.

    Returns:
        int: The location of the pivot.
    """
    n = high - low + 1
    temp  = []
    pivot = arr[high]
    
    for i in range(low, high):
        if arr[i] < pivot:
            temp.append(arr[i])
        
    pivot_index = len(temp) + low # Length of temp = all elements smaller than pivot, low = starting index of subarray
    temp.append(pivot)   
    
    for i in range(low, high):
        if arr[i] >= pivot:
            temp.append(arr[i])
        
    for i in range(n):
        arr[low + i] = temp[i] # low is the starting index of the subarray
        
    return pivot_index
       
    
def quick_sort(arr: list, low: int, high: int, chosen_partition: str = 'hoare') -> None:
    """
    Implements the quick sort algorithm. If the chosen partition is not specified,
    the algorithm uses lomuto partitioning.

    Args:
        arr (list): The input array.
        low (int): The starting index.
        high (int): The ending index.
        chosen_partition (str, optional): The chosen partition to use for the algorithm. Defaults to lomuto.
    """
    if low < high:
        if chosen_partition == 'naive':
            pivot_loc = naive_partition(arr, low, high)
        elif chosen_partition == 'lomuto': 
            pivot_loc = lomuto_partition(arr, low, high)
        else: # Hoare paritition
            pivot_loc = hoare_partition(arr, low, high)

        if chosen_partition == 'hoare': 
            quick_sort(arr, low, pivot_loc)
            quick_sort(arr, pivot_loc + 1, high)
        else: # Naive and Lomuto use the same values
            quick_sort(arr, low, pivot_loc - 1)
            quick_sort(arr, pivot_loc + 1, high)
        