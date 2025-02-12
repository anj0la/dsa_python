import heapq

def job_scheduling(arr: list[list]):
    """
    Implements the job scheduling problem using the greedy approach. The time complexity is 0(N log N) as opposed to 
    O(N^2) with the naive greedy approach by using a max heap to always select the maximum profit.

    Args:
        arr (list[list]): A 2D list where for each job, contains the job id, deadline and profit.

    Returns:
        list[list]: A list containing the job ids, deadlines and profits such that the total profit is maximized.
    """
    res = []
    heap = []
    
    # Sorting the array based on the deadlines
    arr.sort(key=lambda x: x[1])
    
    print(arr)
    
    for i in range(len(arr) - 1, -1, -1):
        # Calculate free slots between two consecutive deadlines
        (free_slots := arr[i][1]) if i == 0 else (free_slots := arr[i][1] - arr[i - 1][1])
        
        print(free_slots)
        
        # Insert the profit, deadline, and job ID of ith job in the max heap
        heapq.heappush(heap, (-arr[i][2], arr[i][1], arr[i][0]))
        
        while free_slots and heap:
            
            # Get the job with the max profit
            profit, deadline, job_id = heapq.heappop(heap)
            
            # Reduce the number of free slots
            free_slots -= 1
            
            # Append the job id, deadline and profit to the result
            res.append([job_id, deadline, -profit])
        
    # Return the result sorted based on deadlines
    return res.sort(key=lambda x: x[1])
            
if __name__ == '__main__':
    jobs = [['a', 2, 100],  # Job Array
              ['b', 1, 19],
              ['c', 2, 27],
              ['d', 1, 25],
              ['e', 3, 15]]
    
    res = job_scheduling(jobs)
    print(res)
    job_ids = [res[i][0] for i in range(len(res))]
    max_profit = sum([res[i][2] for i in range(len(res))])
    
    print(f'Job IDs: {job_ids}, Max Profit: {max_profit}')
    
    
    # 0: [b, 1, 19], 1: [d, 1, 25], 2: [a, 2, 100], 3: [c, 2, 27], 4: [e, 3, 25]
    # i = 4, slots = 3 - 2 = 1
    # heapq.heappush(heap, profit, deadline, job_id) -> heap = [(-25, 3, e)]
    # while slots and heap (slots = 1, heap = [(-25, 3, e)]
    # profit, deadline, job_id = heapq.heappop(heap)
    # -25, 3, e
    # slots -= 1
    # res.append([job_id, deadline])
    # res = [[e, 3]]
    
    # i = 3
    # slots = i - (i - 1) = 2 - 2 = 0
    # slots available here is 0
    # heapq.heappush(heap, profit, deadline, job_id) -> heap = [(-27, 2, c)]
    
    # i = 2
    # slots = i - (i - 1) = 2 - 1 = 1
    # slots available here i 1
    # heapq.heappush(heap, profit, deadline, job_id) -> heap = [(-100, 2, a), (-27, 2, c)]
    
    # while slots and heap
    # res = [[e, 3], [a, 2]]
    
    # i = 1
    # slots = 0
    # heapq.heappush(heap, profit, deadline, job_id) -> heap = [(-27, 2, c), (-25, 1, d)]

    
    # i = 0
    # slots = 1
    # heapq.heappush(heap, profit, deadline, job_id) -> heap = [(-27, 2, c), (-25, 1, d), (-19, 1, b)]
    
    # res = [[e, 3], [a, 2], [c, 2]]
    # res = [[a, 2], [c, 2], [e, 3]]


    
    
    """
    
    Sort the jobs based on their deadlines.
    Iterate from the end and calculate the available slots between every two consecutive deadlines. 
    Insert the profit, deadline, and job ID of ith job in the max heap.
    While the slots are available and there are jobs left in the max heap, include the job ID with maximum profit and deadline in the result.
    Sort the result array based on their deadlines.
    """