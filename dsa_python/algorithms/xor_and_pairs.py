import math

def naive_dominating_xor_pairs(arr: list[int]) -> int:
    """
    Question: For an array arr of n positive integers, count the unordered pairs (i,j) (0 <= i < j < n) where arr[i] XOR arr[j] > arr[i] AND arr[j]. 
    XOR denotes the bitwise XOR operation and AND denotes the bitwise AND operation. 
    """
    # XOR: ^
    # OR: |
    # AND: &
    
    n = len(arr)
    count_pairs = 0
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] ^ arr[j] > arr[i] & arr[j]:
                count_pairs += 1
                
    return count_pairs
       
def optimized_dominating_xor_pairs(arr: list[int]) -> int:
    """
    The this optimized solution utilizes bucket sort, which sorts elements of the array into buckets.
    """
    n = len(arr)
    bits = [0] * 32 # buckets
    
    for i in range(n):
        
        # get the most significant digit
        pos = int(math.log2(arr[i]))
        # increase the count of the bits at that position
        bits[pos] += 1
        
    res = 0
    for i in range(32):
        res = res + int((bits[i] * (bits[i] - 1)) / 2)
        
    return int((n * (n - 1) / 2) - res)
            
    
if __name__ == '__main__':
    arr = [4,3,5,2]
    assert naive_dominating_xor_pairs(arr) == 4 # if False, Assertion error occurs
    assert optimized_dominating_xor_pairs(arr) == 4
    