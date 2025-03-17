def climbing_stairs_recursion(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    
    Constraints:

    1 <= n <= 45
    """
    # Base case
    if n == 0 or n == 1:
        return 1
    
    # Recursion
    return climbing_stairs_recursion(n - 1) + climbing_stairs_recursion(n - 2)

def climbing_stairs(n: int) -> int:
    """
    You are climbing a staircase. It takes n steps to reach the top.
    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    
    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    Example 2:

    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    
    Constraints:

    1 <= n <= 45
    """
    dp = [1 if i == 0 or i == 1 else 0 for i in range(n + 1)]
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
        
    return dp[n]
    
    # objective function - can I break this into subproblems that build the solution?
    # F(i) is the number of ways to reach the ith step.
    
    # Base case
    # F(0) = 1 -> there is 1 way to reach the 0th step
    # F(1) = 1 -> there is 1 way to reach the 1st step: taking 1 step
    # F(2) = 2 -> there are 2 ways to reach the 2nd step: taking 1 step AND another step, or taking two steps
    
    # recurrence
    # F(2) = F(1) + F(0) = 1 + 1 = 2
    # F(3) = F(2) + F(1) = 2 + 1 = 3
    # F(4) = F(3) + F(2) = 3 + 2 = 5
    # F(n) = F(n - 1) + F(n - 2)
    
    # bottom-up (tabulatization), top-down (recursion)
    
    
if __name__ == '__main__':
    assert climbing_stairs_recursion(5) == climbing_stairs(5)
    assert climbing_stairs_recursion(10) == climbing_stairs(10)

    print(climbing_stairs_recursion(2))
    print(climbing_stairs(2))
    print(climbing_stairs_recursion(3))
    print(climbing_stairs(3))