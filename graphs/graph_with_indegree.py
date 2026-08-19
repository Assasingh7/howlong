from collections import defaultdict, deque

def build_graph_with_indegree(edges):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    
    # Process each edge
    for u, v in edges:
        graph[u].append(v)      # 0: Add edge
        in_degree[v] += 1        # 1: Increment in-degree
    
    return graph, in_degree

# Example
edges = [(0, 1), (0, 2), (1, 3), (2, 3), (4, 3)]
graph, in_degree = build_graph_with_indegree(edges)

# graph = {0: [1, 2], 1: [3], 2: [3], 4: [3]}
# in_degree = {1: 1, 2: 1, 3: 3, 0: 0, 4: 0}