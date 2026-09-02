import heapq

# Method to calculate the number of shortest paths from node 0 to node n-1
def countPaths(n, roads, src, dst, K):

    # Create an adjacency list to represent airports and flights as a graph
    adj = {i: [] for i in range(n)}
    for road in roads:
        adj[road[0]].append([road[1], road[2]])
        adj[road[1]].append([road[0], road[2]])

    # Create a priority queue (min heap) for Dijkstra's algorithm
    pq = [(0, 0)]  # Push the source node with distance 0

    # Initialize the distance array and ways array
    dist = [float('inf')] * n
    dist[src] = 0
    ways = [0] * n
    ways[src] = 1

    # Define the modulo value for large numbers
    mod = int(1e9 + 7)

    # Perform Dijkstra's algorithm
    while pq:
        dis, node = heapq.heappop(pq)

        # Iterate through adjacent nodes
        for adjNode, edW in adj[node]:
            # If a shorter path is found, update the distance and number of ways
            if dis + edW < dist[adjNode]:
                dist[adjNode] = dis + edW
                heapq.heappush(pq, (dis + edW, adjNode))
                ways[adjNode] = ways[node]
            # If the same shortest path is found, update the number of ways
            elif dis + edW == dist[adjNode]:
                ways[adjNode] = (ways[adjNode] + ways[node]) % mod

    # Return the number of ways to reach the last node modulo 10^9 + 7
    return ways[dst] % mod

# Main function
def main():
    # Input data
    n = 7
    roads = [[0, 6, 7], [0, 1, 2], [1, 2, 3], [1, 3, 3], [6, 3, 3], 
             [3, 5, 1], [6, 5, 1], [2, 5, 1], [0, 4, 5], [4, 6, 2]]

    # Call the method to count the number of shortest paths
    ans = countPaths(n, roads, 0, 3, 1)

    # Output the result
    print(ans)

# Call the main function
if __name__ == "__main__":
    main()