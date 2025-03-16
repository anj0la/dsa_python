import math
from collections import defaultdict

def char_at(string: str, d: int):
    if len(string) < 1:
        return -1
    return ord(string[d])

def digit_at(x: int, d: int):
    if d <= 0:
        return 0  # Assuming we pad with 0s for missing digits
    return (x // (10 ** (d - 1))) % 10


def count_sort_int(arr: list[int], low: int, high: int, d: int):
    count = [0] * (10 + 2) # Base = 10
    temp = [0] * (high - low + 1)
    
    # Storing occurences in count
    for i in range(low, high + 1):
        c = digit_at(arr[i], d)
        count[c + 2] += 1
        
    # Similar to counting sort (but with i = i + i - 1)
    for j in range(10 + 1):
        count[j + 1] += count[j]
    
    # Similar to building output array, but not reversing it (which makes the sort stable in counting sort)
    for i in range(low, high + 1):
        c = digit_at(arr[i], d)
        temp[count[c + 1]] = arr[i]
        count[c + 1] += 1
        
    # Copying elements from temporaray array to original array
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
        
    return count

def count_sort_str(arr: list[str], low: int, high: int, d: int):
    count = [0] * (256 + 1) # Base = 256
    temp = defaultdict(str)
    
    # Storing occurences in count
    for i in range(low, high + 1):
        c = char_at(arr[i], d)
        count[c + 2] += 1
        
    for j in range(256):
        count[j + 1] += count[j]
    
    for i in range(low, high + 1):
        c = char_at(arr[i], d)
        temp[count[c + 1]] = arr[i]
        count[c + 1] += 1
        
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
        
    return count
    
def msd_sort_int(arr: list[int], low: int, high: int, d: int):
    # Base case
    if high <= low or d <= 0:
        return arr
    # Recursion
    count = count_sort_int(arr, low, high, d) 
    for j in range(10):
        arr = msd_sort_int(arr, low + count[j], low + count[j + 1] - 1, d - 1)
    return arr

def msd_sort_str(arr: list[str], low: int, high: int, d: int):
    # Base case
    if high <= low:
        return arr
    # Recursion
    count = count_sort_str(arr, low, high, d) 
    for j in range(256):
        arr = msd_sort_str(arr, low + count[j], low + count[j + 1] - 1, d - 1)
    return arr
        
def radix_sort_msd(arr: list[int] | list[str]):
    n = len(arr)
    if type(arr[0]) == int:
        m = max(arr)
        d = len(str(abs(m)))
        print(m, d)
        return msd_sort_int(arr, 0, n - 1, d)
    elif type(arr[0]) == str:
        return msd_sort_str(arr, 0, n - 1, 0)
    else:
        raise ValueError('The given array is not a list of integers or a list of strings.')
    
    
# Input array
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print("Unsorted array: ",arr)

# Function Call
arr = radix_sort_msd(arr)

print("Sorted array : ",arr)