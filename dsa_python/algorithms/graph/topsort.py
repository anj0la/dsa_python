from collections import deque
from data_structures.graphs.adj_list import AdjList
from data_structures.graphs.adj_matrix import AdjMatrix

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

def topsort_matrix(graph: AdjMatrix):
    V = len(graph.matrix)
    visited = [False] * V
    ordering = []
    
    def dfs(u):
        visited[u] = True
        
        for v in range(V):
            if graph.matrix[u][v] == 1 and not visited[v]:
                dfs(v)
                
        ordering.append(u)
    
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
            
    ### BFS-ish ###
    queue = deque([i for i in range(V) if in_deg[i] == 0])
    ordering = []
    
    while queue:
        v = queue.popleft()
        ordering.append(v)
        
        for w in graph.adj[v]:
            in_deg[w] -= 1
            if in_deg[w] == 0:
                queue.append(w)
                
    return [] if len(ordering) != V else ordering
    
def kahn_topsort_matrix(graph: AdjMatrix):
    V = len(graph.matrix)
    indeg = [0] * V
    
    for u in range(V):
        for v in range(V):
            if graph.matrix[u][v] == 1:
                indeg[v] += 1
                
    queue = deque([i for i in range(V) if indeg[i] == 0])
    ordering = []
    
    while queue:
        u = queue.popleft()
        ordering.append(u)
        
        for v in range(V):
            if graph.matrix[u][v] == 1:
                indeg[v] -= 1
                if indeg[v] == 0:
                    queue.append(v)
                    
    return ordering if len(ordering) == V else [] # cycle detected
                            
     
            