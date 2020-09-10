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

    graph = {1: set([3, 4]),
              2: set([3, 4, 5]),
              3: set([1, 5]),
              4: set([1]),
              5: set([2, 6]),
              6: set([3, 5])}
              
    node = 1

    dfs(graph, node)