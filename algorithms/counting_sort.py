def counting_sort(arr: list[int], k: int) -> list[int]:
    """
    Implements the counting sort algorithm.

    Args:
        arr (list[int]): The input array (must be an integer array).
        k (int): The maximum value of the list.

    Returns:
        list[int]: The sorted array.
    """
    n = len(arr)
    count_arr = [0] * (k + 1)
    
    for num in arr:
        count_arr[num] += 1
        
    for i in range(1, k + 1):
        count_arr[i] = count_arr[i] + count_arr[i - 1]
        
    output_arr = [0] * n
        
    for i in range(n - 1, -1, -1):
        output_arr[count_arr[arr[i]] - 1] = arr[i]
        count_arr[arr[i]] -= 1
        
    return output_arr