from collections import deque

def bfs(graph, node):
    
    visited = []
    dq = deque([node])

    while dq:
    
        n = dq.popleft()

        if n not in visited:
            visited.append(n)
            dq += graph[n] - set(visited)
    
    return print(visited) 

if __name__ == "__main__":

    graph = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
              
    node = 1

    bfs(graph, node)