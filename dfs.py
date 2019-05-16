graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

def dfs(graph, start, need):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if vertex == need:
            return True

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    print(visited)
    return False

print(dfs(graph, 'A', 'E'))

def dfs2(graph, start, need, visited = None):
    if start == need:
        return True

    if visited is None:
        visited = set()

    visited.add(start)

    for next in graph[start] - visited:
        if (dfs2(graph, next, need, visited)):
            return True

    return False

print(dfs2(graph, 'A', 'G'))

def bfs(graph, start):
    visited = set()
    queue = [start]
    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.add(vertex)
            queue.extend(graph[vertex] - visited)
    return visited

print(bfs(graph, 'A'))


def dfs(graph, start, need, visited = None):
    if visited is None:
        visited = set()

    visited.add(start)

    for next in graph[start] - visited:
        if (dfs(graph, next, need, visited)):
            return True

    return False

def dfs(graph, start, need):
    visited = set()
    stack = [start]

    while stack:
        vertex = stack.pop()
        if start == need:
            return True

        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited)

    return False
