# Q.2 Write a Python program to implement the Depth First Search (DFS) algorithm. Refer to the following graph as input for the program. [Initial node = 2, Goal node = 7]

graph = {
    1: [2, 3],
    2: [1, 4, 5, 6],
    3: [1, 4],
    4: [2, 3, 5],
    5: [2, 4, 6, 7],
    6: [2, 5],
    7: [5]
}

def dfs(graph, start, goal, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start, end=" ")  

    if start == goal:
        return True  

    for neighbor in graph[start]:
        if neighbor not in visited:
            if dfs(graph, neighbor, goal, visited):
                return True
    return False

print("DFS traversal path:")
dfs(graph, 2, 7)


Output:
DFS traversal path:
2 1 3 4 5 7
