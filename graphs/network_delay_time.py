import heapq

class Solution:
    # Function to find minimum time for every node to receive signal
    def networkDelayTime(self, times, n, k):
        # Create adjacency list
        adj = [[] for _ in range(n + 1)]
        for u, v, w in times:
            adj[u].append((v, w))

        # Initialize min-heap
        pq = [(0, k)]

        # Initialize distance array
        dist = [float('inf')] * (n + 1)
        dist[k] = 0

        # Process nodes
        while pq:
            # Pop node with smallest time
            time, node = heapq.heappop(pq)

            # Traverse neighbors of current node
            for nbr, wt in adj[node]:
                # If shorter path is found
                if dist[nbr] > time + wt:
                    # Update distance
                    dist[nbr] = time + wt
                    # Push updated distance to heap
                    heapq.heappush(pq, (dist[nbr], nbr))

        # Get maximum time
        ans = max(dist[1:])
        return -1 if ans == float('inf') else ans

# Main function
if __name__ == "__main__":
    sol = Solution()
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n, k = 4, 2
    print(sol.networkDelayTime(times, n, k))
