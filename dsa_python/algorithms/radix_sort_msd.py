import math
from collections import defaultdict

def char_at(string: str, d: int):
    if len(string) < 1:
        return -1
    return ord(string[d])

def digit_at(x: int, d: int):
    return int((x / math.pow(10, d - 1)) % 10)

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

def count_sort(arr: list[str], low: int, high: int, d: int, base: int):
    is_string = (base == 256)
    count = [0] * (base + 1) if is_string else [0] * (base + 2)
    temp = defaultdict(str) if is_string else defaultdict(int)
    
    # Storing occurences in count
    for i in range(low, high + 1):
        if is_string:
            c = char_at(arr[i], d)
        else:
            c = digit_at(arr[i], d)
        count[c + 2] += 1
        
    stop = base if is_string else base + 1
    for j in range(stop):
        count[j + 1] += count[j]
    
    for i in range(low, high + 1):
        if is_string:
            c = char_at(arr[i], d)
        else:
            c = digit_at(arr[i], d)
        temp[count[c + 1]] = arr[i]
        count[c + 1] += 1
        
    for i in range(low, high + 1):
        arr[i] = temp[i - low]
        
    return count
    
        
def msd_sort(arr: list[int] | list[str], low: int, high: int, d: int, base: int):
    # Base case
    if high <= low:
        return arr
    # Recursion
    count = count_sort(arr, low, high, d, base) 
    for j in range(base):
        arr = msd_sort(arr, low + count[j], low + count[j + 1] - 1, d - 1, base)
    return arr
        
def radix_sort_msd(arr: list[int] | list[str]):
    n = len(arr)
    if type(arr[0]) == int:
        m = max(arr)
        d = int(math.floor(math.log10(abs(m)))) + 1 # Getting the exponential value of maxmium value
        base = 10
    elif type(arr[0]) == str:
        d = 0
        base = 256
    else:
        raise ValueError('The given array is not a list of integers or a list of strings.')
    return msd_sort(arr, 0, n - 1, d, base)
    
    
# Input array
arr = [9330, 9950, 718, 8977, 6790, 95, 9807, 741, 8586, 5710]
print("Unsorted array: ",arr)

# Function Call
arr = radix_sort_msd(arr)

print("Sorted array : ",arr)