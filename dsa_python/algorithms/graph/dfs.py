from data_structures.graphs.adj_list import AdjList
            
def dfs(graph: AdjList, s):
    visited = [False] * len(graph.adj)
    
    def dfs_helper(v):
        visited[v] = True
        
        for w in graph.adj[v]:
            if not visited[w]:
                dfs_helper(w)
    
    dfs_helper(s)
        
def dfs_recursive_return(graph: AdjList, s):
    visited = set()
    
    def dfs_helper(v):
        if v not in visited:
            visited.add(v)
        
            for w in graph.adj[v]:
                dfs_helper(w)
                    
    dfs_helper(s)
    return visited

def dfs_stack(graph, s):
    visited = {s}
    stack = [s]
    
    while stack:
        v = stack.pop()
        
        for w in graph.adj[v]:
            if w not in visited:
                stack.append(w)
                visited.add(w)
                
    return visited