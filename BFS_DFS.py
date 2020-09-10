import queue

def bfs(graph, node):
    
    visited = []
    queue = [node]

    while queue:
        
        n = queue.pop(0)

        if n not in visited:
            visited.append(n)
            queue += graph[n] - set(visited)
    
    return print(visited) 

def dfs(graph, node):

    visited = []
    stack = [node]

    while stack:
        
        n = stack.pop()

        if n not in visited:
            visited.append(n)
            stack += graph[n] - set(visited)

    return print(visited)

if __name__ == "__main__":

    graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
              
    node = 'A'

    print("BFS 경로")
    bfs(graph, node)

    print("DFS 경로")
    dfs(graph, node)
