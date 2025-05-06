from collections import deque
from data_structures.graphs.adj_list import AdjList

def topsort(graph: AdjList):    
    V = len(graph.adj)
    ordering = []
    visited = [False] * V
    
    ### DFS ###
    def dfs(v):
        visited[v] = True
        
        for i in graph.adj[v]:
            if not visited[i]:
                dfs(i)
                
        ordering.append(v)
        
    ### TOP SORT ###
    for i in range(V):
        if not visited[i]:
            dfs(i)
            
    return ordering[::-1]

def kahn_topsort(graph: AdjList):
    
    ### IN_DEG ###
    V = len(graph.adj)
    in_deg = [0] * V
    
    for u in range(V):
        for v in graph.adj[u]:
            in_deg[v] += 1
            
    ### BFS ###
    queue = deque([i for i in V if in_deg[i] == 0])
    ordering = []
    
    while queue:
        v = queue.popleft()
        ordering.append(v)
        
        for w in graph.adj[v]:
            in_deg[w] -= 1
            if in_deg[w] == 0:
                queue.append(w)
                
    return [] if len(ordering) != V else ordering
    
    
            
                            
     
            