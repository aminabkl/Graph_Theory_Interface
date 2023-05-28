# def kosaraju(graph):
#     def dfs_util(node, visited, stack):
#         visited[node] = True

#         for neighbor in graph[node]:
#             if not visited[neighbor]:
#                 dfs_util(neighbor, visited, stack)

#         stack.append(node)

#     def dfs_util_reverse(node, visited, component):
#         visited[node] = True
#         component.append(node)

#         for neighbor in graph_reverse[node]:
#             if not visited[neighbor]:
#                 dfs_util_reverse(neighbor, visited, component)

#     # Step 1: Perform Depth First Search (DFS) and create the stack
#     num_nodes = len(graph)
#     visited = [False] * num_nodes
#     stack = []
#     for node in range(num_nodes):
#         if not visited[node]:
#             dfs_util(node, visited, stack)

#     # Step 2: Reverse the graph
#     graph_reverse = [[] for _ in range(num_nodes)]
#     for node in range(num_nodes):
#         for neighbor in graph[node]:
#             graph_reverse[neighbor].append(node)

#     # Step 3: Perform DFS on the reversed graph and get strongly connected components
#     visited = [False] * num_nodes
#     strongly_connected_components = []
#     while stack:
#         node = stack.pop()
#         if not visited[node]:
#             component = []
#             dfs_util_reverse(node, visited, component)
#             strongly_connected_components.append(component)

#     return strongly_connected_components


def kosaraju(graph, start_node):
    def dfs_util(node, visited, stack):
        visited[node] = True

        for neighbor in graph[node]:
            if not visited[neighbor]:
                dfs_util(neighbor, visited, stack)

        stack.append(node)

    def dfs_util_reverse(node, visited, component):
        visited[node] = True
        component.append(node)

        for neighbor in graph_reverse[node]:
            if not visited[neighbor]:
                dfs_util_reverse(neighbor, visited, component)

    # Step 1: Perform Depth First Search (DFS) and create the stack
    num_nodes = len(graph)
    visited = [False] * num_nodes
    stack = []
    dfs_util(start_node, visited, stack)

    # Step 2: Reverse the graph
    graph_reverse = [[] for _ in range(num_nodes)]
    for node in range(num_nodes):
        for neighbor in graph[node]:
            graph_reverse[neighbor].append(node)

    # Step 3: Perform DFS on the reversed graph and get strongly connected components
    visited = [False] * num_nodes
    strongly_connected_components = []
    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs_util_reverse(node, visited, component)
            strongly_connected_components.append(component)

    return strongly_connected_components
