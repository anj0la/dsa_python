def maximum_sum_subarray(arr: list[int], k: int) -> int:
    """
    Given an array of integers of size ‘n’, Our aim is to calculate the maximum sum of ‘k’ consecutive elements in the array.
    """
    if len(arr) <= k:
        return -1
    
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    for i in range(len(arr) - k): # iterate through input list
        window_sum = window_sum - arr[i] + arr[i + k] # contract the window (i.e., arr[i]) and expand the window (i.e., arr[i + k])
        max_sum = max(max_sum, window_sum) # process the window
        
    return max_sum
    
if __name__ == '__main__':
    arr = [100,200,300,400]
    k = 2
    print(maximum_sum_subarray(arr, k))
    
            