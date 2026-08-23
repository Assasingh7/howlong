from collections import deque

def eventualSafeNodes(graph):

    n = len(graph)

    # Reverse graph
    reverse = [[] for _ in range(n)]

    # outdegree of each node
    outdegree = [0] * n

    for u in range(n):

        # Number of outgoing edges
        outdegree[u] = len(graph[u])

        for v in graph[u]:

            # Original:
            # u → v
            #
            # Reverse:
            # v → u
            reverse[v].append(u)

    q = deque()

    # Nodes with no outgoing edges are immediately safe
    for node in range(n):

        if outdegree[node] == 0:
            q.append(node)

    safe = [False] * n

    while q:

        node = q.popleft()

        safe[node] = True

        # Look at nodes that point INTO this safe node
        for prev in reverse[node]:

            # One outgoing edge of prev
            # now leads to a known safe node
            outdegree[prev] -= 1

            # All outgoing edges of prev
            # now lead to safe nodes
            if outdegree[prev] == 0:
                q.append(prev)

    return [i for i in range(n) if safe[i]]