from data_structures.graphs.adj_matrix import AdjMatrix

def dfs(graph: AdjMatrix, s):
    V = len(graph.matrix)
    visited = [False] * V
    
    def dfs_helper(u):
        visited[u] = True
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and not visited[v]:
                dfs_helper(v)
    
    dfs_helper(s)
    
    
def dfs_ret(graph: AdjMatrix, s):
    V = len(graph.matrix)
    visited = set()
    
    def dfs_helper(u):
        visited.add(u)
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and v not in visited:
                dfs_helper(v)

    dfs_helper(s)
    return visited

def dfs_stack(graph: AdjMatrix, s):
    V = len(graph.matrix)
    stack = [s]
    visited = [False if i != s else True for i in range (V)]
    
    while stack:
        u = stack.pop()
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and not visited[v]:
                visited[v] = True
                stack.append(v)
   
def dfs_stack_ret(graph: AdjMatrix, s):
    V = len(graph.matrix)
    stack = [s]
    visited = {s}
    
    while stack:
        u = stack.pop()
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and v not in visited:
                visited.add(v)
                stack.append(v)
                
    return visited