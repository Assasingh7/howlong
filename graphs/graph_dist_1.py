from collections import deque

def shortestPath(n, adj, src):

    # -1 means node has not been reached yet
    dist = [-1] * n

    # Source is 0 distance away from itself
    dist[src] = 0

    q = deque()

    # Start BFS from source
    q.append(src)

    while q:

        node = q.popleft()

        for neighbor in adj[node]:

            # Haven't reached this node before
            if dist[neighbor] == -1:

                # One edge farther than current node
                dist[neighbor] = dist[node] + 1

                q.append(neighbor)

    return dist