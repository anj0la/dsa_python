"""
Problem: Given a set of coin values coins = {c1, c2, c3, ..., ck} and a target sum of money m, what is the minimum number of coins
that form the sum m?

Source: https://www.youtube.com/watch?v=Hdr64lKQ3e4

Code Explanation:

The base case occurs when no more coins are required to form an empty sum. Therefore, the answer is 0.
Otherwise, the answer is None, so we must go through each coin and do the following:
    - Get the subproblem.
    - Get the minimum from the current answer and the subproblem.
        
Some subproblems will give us negative values. We want to skip those subproblems, so we ignore them entirely.

Example: coins = [1, 4, 5], m = 13

One call of minimum_coins is as follows:

minimum_coins([1, 4, 5], 13)
answer = None
for coin in [1, 4, 5]: # Assume coin = 1
    subproblem = 13 - 1 = 12
    if 12 >= 0 continue so,
    answer = min_ignore_none(None, minimum_coins[[1, 4, 5], 12] + 1) # The + 1 increments the amount of coins we have used so far
return answer
"""

def min_ignore_none(a: int, b: int) -> int:
    if not a:
        return b
    if not b:
        return a
    return min(a, b)

def minimum_coins(coins: int, m: int) -> int:
    # Base case occurs when no more coins are required
    if m == 0:
        answer = 0
    else:
        # Otherwise, get the answer from the subproblems
        answer = None
        for coin in coins:
            # Example: if m = 13, then the  subproblems for each coin are as follows: (13 - 5) = 8, (13 - 4) = 9, (13 - 1) = 12           
            subproblem = m - coin 
            # Skip solutions where we try to reach m from a negative subproblem
            if subproblem >= 0: 
                answer = min_ignore_none(answer, minimum_coins(coins, subproblem) + 1)
    return answer

def minimum_coins_tail(coins: int, m: int, curr_answer: int = 0, best_answer: int | None = None) -> int:
     # Base case occurs when no more coins are required
    if m == 0:
        return curr_answer
    # Ignore negative subproblems, so return the best answer  
    if m < 0:
        return best_answer
    else:
        for coin in coins:
            subproblem = m - coin 
            candidate_answer = minimum_coins_tail(coins, subproblem, curr_answer + 1, best_answer)
            
            # Update the best answer
            if best_answer is None or (candidate_answer is not None and candidate_answer < best_answer):
                best_answer = candidate_answer
                
    return 

def minimum_coins_memo_helper(coins, m, memo):
    # If answer has already been computed, return it
    if memo[m]:
        return memo[m]
    # Base case occurs when no more coins are required
    if m == 0:
        answer = 0
    else:
        # Otherwise, get the answer from the subproblems
        answer = None
        for coin in coins:
            # Example: if m = 13, then the  subproblems for each coin are as follows: (13 - 5) = 8, (13 - 4) = 9, (13 - 1) = 12
            subproblem = m - coin
            # Skip solutions where we try to reach m from a negative subproblem
            if subproblem >= 0: 
                answer = min_ignore_none(answer, minimum_coins(coins, subproblem) + 1)  
    # Caching the result so when we see it again, we return the cached result      
    memo[m] = answer 
    return answer

def minimum_coins_memo(coins, m):
    memo = [None] * (m + 1)
    return minimum_coins_memo_helper(coins, m, memo)

def minimum_coins_tail(coins: int, m: int, curr_answer: int = 0, best_answer: int | None = None):
     # Base case occurs when no more coins are required
    if m == 0:
        return curr_answer
    # Ignore negative subproblems, so return the best answer  
    if m < 0:
        return best_answer
    else:
        for coin in coins:
            subproblem = m - coin # The current subproblem
            answer = minimum_coins_tail(coins, subproblem, curr_answer + 1, best_answer)
            
            if best_answer is None or (answer is not None and answer < best_answer):
                best_answer = answer
                
    return best_answer

def main():
    coins = [1, 4, 5]
    m = 13
    print(f'minimum_coins({coins}, {m}) = {minimum_coins(coins, m)}')
    print(f'minimum_coins_tail({coins}, {m}) = {minimum_coins_tail(coins, m)}')
    print(f'minimum_coins_memo({coins}, {m}) = {minimum_coins_memo(coins, m)}')

    
if __name__ == '__main__':
   main()
