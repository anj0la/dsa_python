def number_of_unique_paths(m: int, n: int) -> int:
    """
    You are given an m x n grid. You start at the top-left corner (0,0) and must reach the bottom-right (m-1, n-1), moving only down or right at each step.
    How many different paths exist?
    
    Input: m = 3, n = 7
    Output: 28
    """
    
    # define the objective function / dp state
    # dp[i][j] represents the number of unique paths to reach cell (i, j).
    
    # (0,0) -> 1
    
    # 2 x 2 grid [0 0
    #             0 0] (1,1)
    
    # recurrence relation
    # when at (i,j), you can only come from ABOVE or the LEFT
    # dp[i][j] = dp[i - 1][j] + dp[i][j - 1]   
    
    dp = [[0] * (n) for _ in range(m)]
    
    # row
    for i in range(m):
        dp[i][0] = 1
            
    # col    
    for j in range(n):
        dp[0][j] = 1
        
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            
    return dp[m - 1][n - 1]
    
def unique_paths_with_obstacles(obstacle_grid: list[list[int]]) -> int:
    """
    You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). 
    The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

    An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

    Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
    """
    if obstacle_grid[0][0] == 1:
        return 0

    m = len(obstacle_grid)
    n = len(obstacle_grid[0])

    dp = [[0] * n for _ in range(m)]

    for i in range(m):
        if obstacle_grid[i][0] == 1:
            break
        dp[i][0] = 1

    for j in range(n):
        if obstacle_grid[0][j] == 1:
            break
        dp[0][j] = 1
        
    for i in range(1, m):
        for j in range(1, n):
            if obstacle_grid[i][j] != 1:
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
            else:
                dp[i][j] = 0

        return dp[m - 1][n - 1]  

if __name__ == '__main__':
    print(number_of_unique_paths(3, 7))
    

