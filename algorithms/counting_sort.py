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


def sort_string(arr: list[str]) -> list[str]:
    """
    Sorts a string of characters (string array) lexiographically using counting sort.

    Args:
        arr (list[str]): The input string (or array of characters)

    Returns:
        list[str]: The sorted string.
    """
    n = len(arr)
        
    # Convert the strings into their unicode values
    arr = [(ord(arr[i]) - ord('a') + 1) for i in range(n)] # E.g., arr[i] = a, ord('a') - ord('a') + 1 = 97 - 97 + 1 = 1
    
    # Call counting_sort on the array
    output_array = counting_sort(arr, n)
    
    # Convert the strings (as integers) back into their original format
    output_array = [chr(output_array[i] + (ord('a') - 1)) for i in range(n)]
    
    return ''.join(output_array)
            
# Testing the sort strings function only
string = 'supercalifragilisticexpialidocious'
sorted_string = sort_string(string)
print(f'String: {string}\nSorted: {sorted_string}')