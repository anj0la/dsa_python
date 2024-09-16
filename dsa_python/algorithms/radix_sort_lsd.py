def count_sort(arr: list[int], exp: int) -> None:
    """
    Implements counting sort for radix sort.

    Args:
        arr (list[int]): The input array
        exp (int): The expoential value.
    """
    n = len(arr)
    
    count = [0] * 10 # b = 10
    out = [0] * n
    
    # Storing occurences in count
    for i in range(n):
        idx = arr[i] // exp
        count[idx % 10] += 1
        
    # Changing count so count[i] contains the actual position of the digit in the output array
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    # Build output array
    for i in range(n - 1, -1, -1):
        idx = arr[i] // exp
        out[count[idx % 10] - 1] = arr[i]
        count[idx % 10] -= 1
    
    # Copying outout array to original array
    for i in range(n):
        arr[i] = out[i]

def radix_sort_lsd(arr: list[int]) -> None:
    """
    Implements radix sort using the least significant digits.
    Digits are sorted in their correct locations using counting sort.

    Args:
        arr (list[int]): The input array.
    """
    m = max(arr)
    exp = 1
    
    while m // exp > 0:
        count_sort(arr, exp)
        exp *= 10