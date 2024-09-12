import random
from datetime import datetime
from bubble_sort import bubble_sort, bubble_sort_optimized
from selection_sort import selection_sort, stable_selection_sort

# Constants
MAX_VALUE = 10
SORTING_ALGORITHMS = {
        'Bubble Sort': bubble_sort,
        'Optimized Bubble Sort': bubble_sort_optimized,
        'Selection Sort': selection_sort,
        'Stable Selection Sort': stable_selection_sort
    }

def create_int_array(max_value: int) -> list[int]:
    """
    Creates a random array with max_value integer elements. 

    Args:
        max_value (int): The size (and potential max element) of the random array.

    Returns:
        list[int]: A list of integer values, ranging from 0 to max_value.
    """
    return [random.randint(0, max_value) for _ in range(max_value)]

def test_sorting_algorithms(arr: list, algorithms: dict) -> None:
    """
    Tests all sorting algorithms passed in the algorithms parameter.

    Args:
        arr (list): The array to perform the sorting operations on.
        algorithms (dict): The dictonary containing all the algoirmths to test. 
    """
    print(f'Original Array: {arr[:10]}... (showing first 10 elements)')
    
    for name, sort_function in algorithms.items():
        test_arr = arr.copy()  # Copy the array for each algorithm
        start_time = datetime.now().timestamp()
        
        sort_function(test_arr)  # Sort using the given function
        
        end_time = datetime.now().timestamp()
        elapsed_time = end_time - start_time
        
        print(f'\n{name} sorted array: {test_arr[:10]}... (first 10 elements)')
        print(f'{name} elapsed time: {elapsed_time:.6f} seconds')
        
def main():
    """
    Entry point to run the script.
    """
    random.seed(None)
    # Create a random intger array
    arr = create_int_array(MAX_VALUE)
    
    # Test the sorting algorithms
    test_sorting_algorithms(arr, SORTING_ALGORITHMS)
        
# Main
if __name__ == '__main__':
    main()
    
