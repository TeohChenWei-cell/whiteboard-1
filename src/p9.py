graph = {
    'A': ['B', 'H'],
    'B': ['A', 'D', 'C'],
    'C': ['F'],
    'D': ['E'],
    'E': ['F'],
    'F': ['A', 'B', 'G'],
    'G': [],
    'H': []
}

def dfs(graph, start, end, path=[]):
    path = path + [start]  
    if start == end:
        return True, path  
    if start not in graph:
        return False, []  
    for neighbor in graph[start]:
        if neighbor not in path:  
            found, new_path = dfs(graph, neighbor, end, path)
            if found:
                return True, new_path  
    return False, []

start = 'D' #change this to any from A to H
end = 'B' #change this to any from A to H
found, path = dfs(graph, start, end)
print(f"Expected Output: {found}, Path: {path}")
