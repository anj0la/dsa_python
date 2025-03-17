def sliding_window(input: list) -> None:
    """
    Defines the technique used to solve sliding window problems.
    """
    # Define left and right pointers (two-pointer approach) to create a window
    left = right = 0
    # Define given condition for problem
    some_condition = None
    
    # Iterate over the input list
    while right < len(input):
        # Expand the window 
        
        # Meet condition to stop expansion
        while some_condition:
            # Process the current window
            
            # Contract the window
            left += 1
            
        right += 1
        
    # Handle edge cases
    if not some_condition:
        pass 
    
    # Return the value of the problem
            
def max_consecutive_ones(nums: list[int]) -> int:
    """
    Given a binary array nums, return the maximum number of consecutive 1's in the array.
    
    Example 1:

    Input: nums = [1,1,0,1,1,1]
    Output: 3
    Explanation: The first two digits or the last three digits are consecutive 1s. The maximum number of consecutive 1s is 3.
    Example 2:

    Input: nums = [1,0,1,1,0,1]
    Output: 2
    
    Link: https://leetcode.com/problems/max-consecutive-ones/description/
    """
    # Define left and right pointers (two-pointer approach) to create a window
    left = right = 0
    # Define given condition for problem
    num_zeros = 0
    
    # Returning maximum length as described
    max_len = 0
    
    # Iterate over the input list
    while right < len(nums):
        # Expand the window 
        if nums[right] == 0:
            num_zeros += 1
            
        # Meet condition to stop expansion
        while num_zeros == 1:
            # Process the current window
            max_len = max(max_len, right - left)
            # Contract the window
            if nums[left] == 0:
                num_zeros -= 1
            
            left += 1
            
        right += 1
        
    # Handle edge cases
    if num_zeros < 1:
        max_len = max(max_len, right - left)
 
    # Return the value of the problem
    return max_len

def max_consecutive_ones_ii(nums: list[int]) -> int:
    """
    Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.
  
    Example 1:

    Input: [1,0,1,1,0]
    Output: 4     

    Link (Premium): https://leetcode.com/problems/max-consecutive-ones-ii/
    """
    # Define left and right pointers (two-pointer approach) to create a window
    left = right = 0
    # Define given condition for problem
    num_zeros = 0
    
    # Returning maximum length as described
    max_len = 0
    
    # Iterate over the input list
    while right < len(nums):
        # Expand the window 
        if nums[right] == 0:
            num_zeros += 1
            
        # Meet condition to stop expansion
        while num_zeros == 2:
            # Process the current window
            max_len = max(max_len, right - left)
            # Contract the window
            if nums[left] == 0:
                num_zeros -= 1
            
            left += 1
            
        right += 1
        
    # Handle edge cases
    if num_zeros < 2:
        max_len = max(max_len, right - left)
 
    # Return the value of the problem
    return max_len

def max_consecutive_ones_iii(nums: list[int]) -> int:
    """
    Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

    Example 1:

    Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
    Output: 6
    Explanation: [1,1,1,0,0,1,1,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
    Example 2:

    Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
    Output: 10
    Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
    Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

    Link: https://leetcode.com/problems/max-consecutive-ones-iii/description/
    """
    # Define left and right pointers (two-pointer approach) to create a window
    left = right = 0
    # Define given condition for problem
    num_zeros = 0
    
    # Returning maximum length as described
    max_len = 0
    
    # Iterate over the input list
    while right < len(nums):
        # Expand the window 
        if nums[right] == 0:
            num_zeros += 1
            
        # Meet condition to stop expansion
        while num_zeros > k:
            # Process the current window
            max_len = max(max_len, right - left)
            # Contract the window
            if nums[left] == 0:
                num_zeros -= 1
            
            left += 1
            
        right += 1
        
    # Handle edge cases
    if num_zeros <= k:
        max_len = max(max_len, right - left)
 
    # Return the value of the problem
    return max_len