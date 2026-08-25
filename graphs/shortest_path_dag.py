# Import required modules
from collections import defaultdict, deque

# Define the Solution class
class Solution:

    # Function to perform DFS and generate topological order
    def topoSort(self, node, visited, stack, adj):
        
        # Mark the current node as visited
        visited[node] = True

        # Traverse all the neighbors of the current node
        for neighbor, weight in adj[node]:
            
            # If the neighbor hasn't been visited, call DFS on it
            if not visited[neighbor]:
                self.topoSort(neighbor, visited, stack, adj)

        # Push the current node to stack after visiting all its neighbors
        stack.append(node)

    # Function to find shortest path from source (node 0)
    def shortestPath(self, N, M, edges):
        
        # Create adjacency list with weights
        adj = defaultdict(list)
        for u, v, wt in edges:
            adj[u].append((v, wt))
        
        # Initialize visited array and stack for topological sort
        visited = [False] * N
        stack = []

        # Call topoSort on all unvisited nodes
        for i in range(N):
            if not visited[i]:
                self.topoSort(i, visited, stack, adj)

        # Initialize distance array with infinity
        dist = [float('inf')] * N

        # Distance to source is zero
        dist[0] = 0

        # Process nodes in topological order
        while stack:
            node = stack.pop()

            # Only process nodes that are reachable
            if dist[node] != float('inf'):
                
                # Traverse all neighbors of the current node
                for neighbor, weight in adj[node]:
                    
                    # Relax the edge if a shorter path is found
                    if dist[node] + weight < dist[neighbor]:
                        dist[neighbor] = dist[node] + weight

        # Convert unreachable distances from inf to -1
        for i in range(N):
            if dist[i] == float('inf'):
                dist[i] = -1

        # Return the shortest path distances
        return dist

# Driver code
if __name__ == "__main__":

    # Number of nodes and edges
    N = 6
    M = 7

    # List of edges with weights
    edges = [
        [0,1,2],[0,4,1],[4,5,4],
        [4,2,2],[1,2,3],[2,3,6],[5,3,1]
    ]

    # Create object of Solution class
    obj = Solution()

    # Call the function and store the result
    result = obj.shortestPath(N, M, edges)

    # Print the result
    print(' '.join(map(str, result)))
