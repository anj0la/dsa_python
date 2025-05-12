from collections import deque
from data_structures.graphs.adj_list import AdjList
from data_structures.graphs.adj_matrix import AdjMatrix

def has_cycle(edge_list: list[list[int]], n: int) -> bool:
    parent = list(range(n))
    rank = [0] * n
    
    for u, v in edge_list:
        if find(parent, u) == find(parent, v):
            return True
        
        union(parent, rank, u, v)

def find(parent, i):
    if parent[i] == i:
        return i
    
    parent[i] = find(parent[i])
    return parent[i]

def union(parent, rank, i, j):
    i_root = find(i)
    j_root = find(j)
    
    if i_root == j_root: return
    
    if rank[i_root] < rank[j_root]:
        parent[i_root] = j_root
    elif rank[i_root] > rank[j_root]:
        parent[j_root] = i_root
    else:
        parent[j_root] = i_root
        rank[i_root] += 1
    
## Detecting cycle in undirected graph using DFS 
def has_cycle_dfs(graph: AdjList):
    visited = [False] * len(graph.adj)
    
    def dfs(u, parent):
        visited[u] = True
        
        for v in graph.adj[v]:
            if not visited[v]:
                if dfs(v, u):
                    return True
            elif v != parent:
                return True # Found cycle
            
        return False
    
    for u in range(len(graph.adj)):
        if not visited[u]:
            if dfs(u, -1):
                return True
    return False

## Detecting cycle in undirected graph using BFS
def has_cycle_bfs(graph: AdjList):
    visited = [False] * len(graph.adj)
    
    def bfs(s):
        queue = deque([(s, -1)])
        visited[s] = True
        
        while queue:
            u, parent = queue.popleft()
            
            for v in graph.adj[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append((v, u))
                elif v != parent:
                    return True # Found a cycle
                
        return False

    for u in range(len(graph.adj)):
        if not visited[u]:
            if bfs(u):
                return True
    return False
 
## Detecting cycle in directed graph using DFS
def has_cycle_directed(graph: AdjList):
    visited = [False] * len(graph.adj)
    rec = [False] * len(graph.adj)
    
    def dfs(u):
        visited[u] = True
        rec[u] = True
        
        for v in graph.adj[u]:
            if not visited[v]:
                if dfs(v):
                    return True
            elif rec[v]:
                return True # Found cycle
            
        rec[u] = False # Backtrack
        return False
    
    for i in range(len(graph.adj)):
        if not visited[i]:
            if dfs(i):
                return True
            
    return False