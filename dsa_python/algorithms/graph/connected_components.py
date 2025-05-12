from data_structures.graphs.adj_list import AdjList
from data_structures.graphs.adj_matrix import AdjMatrix

def get_components(G: AdjList):
    
    ### DFS (recursive) ###
    def dfs(v, comp):
        visited[v] = True
        comp.append(v)
        
        for w in G.adj[v]:
            if not visited[w]:
                dfs(w, comp)
       
    ### Connected Components (UNDIRECTED) ### 
    V = len(G.adj)
    visited = [False] * V
    res = []
    
    for i in range(V):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            res.append(comp)
            
    return res
            
def get_components_stack(G: AdjList):
    
    def dfs(v, comp):
        st = [v]
        
        while st:
            u = st.pop()
            if not visited[u]:
                visited[u] = True
                comp.append(u)
            
                for w in G.adj[u]:
                    st.append(w)
                    
    V = len(G.adj)
    visited = [False] * V
    res = []
    
    for i in range(V):
        if not visited[i]:
            comp = []
            dfs(i, comp)
            res.append(comp)
            
    return res
                    
def strongly_connected(G: AdjList):
    
    def dfs(v):
        # We make time a nonlocal variable so that changes made here affect the outer variable
        nonlocal time
        # Initialize discovery time and low-link value of the node to be the current discovery time
        disc[v] = low[v] = time
        time += 1
        # Push the node onto the stack and mark that it is currently on the stack
        stack_member[v] = True 
        stack.append(v)
        
        # For each adjacent node do the following
        for w in G.adj[v]:
            if disc[w] == -1:
                dfs(w)
                # If w (a child of v) can reach an ancestor of v (i.e., a node "above" v),
                # Then v can also reach that ancestor through w.
                # Update v's low-link value to reflect this.
                low[v] = min(low[v], low[w])
            elif stack_member[w]:
                # If w is already on the stack, it's part of the current DFS path.
                # That means we've found a cycle back to an ancestor.
                # Update v's low-link value using w's discovery time.
                low[v] = min(low[v], disc[w])
              
        # Found an SCC with v as the root
        if low[v] == disc[v]:
            comp = []
            # Pop nodes from the stack until v is reached
            while True:
                u = stack.pop()
                stack_member[u] = False
                comp.append(u)
                if v == u:
                    break
            
            # Append the SCC to the result
            res.append(comp)
    
    # Mark all vertices as not visited (i.e., the disc node)
    # Mark all low-links as -1 (indicates that no low-link values has been assigned)
    # Set the global time variable to be 0, used to track discovery time
    # Set the stack to be initially empty, along with the stack_member variable to track current verticies on the stack
    # Store the result (if necessary)
    V = len(G.adj)
    time = 0
    stack = []
    stack_member = [False] * V
    disc = [-1] * V
    low = [-1] * V
    res = []
    
    # For each unvisited node, call DFS (that's what disc represents instead of the regular visited var)
    for i in range(V):
        if disc[i] == -1:
            dfs(i)
            
    return res

def get_components_union(edge_list: list[list[int]], n: int) -> list:
    parent = list(range(n))
    rank = [0] * n
    
    for u, v in edge_list:
        union(parent, rank, u, v)
        
    for i in range(n):
        parent[i] = find(parent, i)
        
    res = {}
    
    for i in range(n):
        root = parent[i]
        if root not in res:
            res[root] = []
            
        res[root].append(i)
        
    return list(res.values())

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
        
def get_components_matrix(G: AdjMatrix):
    V = len(G.matrix)
    visited = [False] * V
    res = []
    
    def dfs(u, comp):
        visited[u] = True
        comp.append(u)
        
        for v in range(V):
            if G.matrix[u][v] == 1 and not visited[v]:
                dfs(v, comp)
    
    for i in range(V):
        if not visited[i]:
            comp = []
            dfs(i)
            res.append(comp)
            
    return res