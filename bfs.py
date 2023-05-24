from collections import deque

# def bfs(graph, start):
#     visited = [False] * len(graph)
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")
#         for neighbor in range(len(graph)):
#             if graph[node][neighbor] == 1 and not visited[neighbor]:
#                 queue.append(neighbor)
#                 visited[neighbor] = True

# def bfs(graph, start):
#     visited = [False] * len(graph)
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         print(node, end=" ")
#         for neighbor in graph.neighbors(node):
#             if not visited[neighbor]:
#                 queue.append(neighbor)
#                 visited[neighbor] = True


# def bfs(graph, start):
#     visited = [False] * len(graph)
#     result = []
#     queue = deque([start])
#     visited[start] = True
#     while queue:
#         node = queue.popleft()
#         result.append(node)
#         for neighbor in range(len(graph)):
#             if graph[node][neighbor] == 1 and not visited[neighbor]:
#                 queue.append(neighbor)
#                 visited[neighbor] = True
#     return result

def bfs(graph, start):
    visited = [False] * len(graph.nodes)
    queue = deque([start])
    visited[start] = True
    result = []
    while queue:
        node = queue.popleft()
        result.append(node)
        for neighbor in graph.neighbors(node):
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True
    return result
