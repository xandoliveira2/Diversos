from collections import deque

def bfs(start, is_goal, neighbors_of):
    """
    start: the start node (e.g., (r,c) in a grid, or an id in a graph)
    is_goal(node) -> bool: tells if node is the goal
    neighbors_of(node) -> iterable: yields neighbors of node
    """
    q = deque([start]) # q = Deque(['A'])
    visited = {start} # visited = {'A'}
    parent = {start: None} # parent = {'A' : None}

    while q: #enquanto tiver dados na fila:
        u = q.popleft() # u = 'A'            
        if is_goal(u): # 'A' == 'E' ?
            path = [] 
            cur = u 
            while cur is not None: 
                path.append(cur) 
                cur = parent[cur] 
            path.reverse()
            return path               

        for v in neighbors_of(u): # for v in neighbors_of(u) -> for v in ['B','C']  |  v in ['C']
            if v not in visited: # if b not in visited:                             |  if v not in visited:
                visited.add(v)   # visited.add('B')                                 |       visited.add('C')
                parent[v] = u    # parent['B'] = 'A'                                |       parent['C'] = 'A'
                q.append(v)      # q.append('B')                                    |       q.ppend('C')

    return None  # no path


graph = {
    'A': ['B','C'],
    'B': ['A','D'],
    'C': ['A','D'],
    'D': ['B','C','E'],
    'E': []
}

path = bfs(
    start='A',
    is_goal=lambda x: x == 'E',
    neighbors_of=lambda x: graph.get(x, [])
)
