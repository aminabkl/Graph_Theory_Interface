# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = [False] * len(graph)
#     visited[start] = True
#     print(start, end=" ")
#     for neighbor in range(len(graph)):
#         if graph[start][neighbor] == 1 and not visited[neighbor]:
#             dfs(graph, neighbor, visited)


# def dfs(graph, start, visited=None):
#     if visited is None:
#         visited = [False] * len(graph.nodes)
#     visited[start] = True
#     print(start, end=" ")
#     for neighbor in graph.successors(start):
#         if not visited[neighbor]:
#             dfs(graph, neighbor, visited)

# def dfs(graph, start):
#     visited = [False] * len(graph)
#     result = []
#     stack = [start]
#     visited[start] = True
#     while stack:
#         node = stack.pop()
#         result.append(node)
#         for neighbor in range(len(graph)):
#             if graph[node][neighbor] == 1 and not visited[neighbor]:
#                 stack.append(neighbor)
#                 visited[neighbor] = True
#     return result

def dfs(graph, node, visited=None):
    if visited is None:
        visited = set()
    visited.add(node)
    print(node, end=" ")
    for neighbor in graph.neighbors(node):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)
    return visited
