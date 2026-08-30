from collections import deque

# Method to find the cheapest flight within K stops using BFS
def CheapestFLight(n, flights, src, dst, K):

    # Create an adjacency list to represent airports and flights as a graph
    adj = {i: [] for i in range(n)}
    for flight in flights:
        adj[flight[0]].append([flight[1], flight[2]])

    # Create a queue to store the node, its distance from the source, and the number of stops
    q = deque([(0, src, 0)])  # Push the source node with 0 stops and 0 cost

    # Create a distance array to store the minimum cost to reach each node
    dist = [float('inf')] * n
    dist[src] = 0

    # BFS traversal with a queue to process the nodes
    while q:
        stops, node, cost = q.popleft()

        # If the number of stops exceeds K, continue to the next iteration
        if stops > K:
            continue

        # Iterate over all the adjacent nodes (next destinations)
        for adjNode, edW in adj[node]:
            # If a shorter path to the adjacent node is found, update the distance
            if cost + edW < dist[adjNode] and stops <= K:
                dist[adjNode] = cost + edW  # Update the distance
                q.append((stops + 1, adjNode, cost + edW))  # Push the new node with updated stops and cost

    # If destination node is unreachable, return -1
    if dist[dst] == float('inf'):
        return -1

    return dist[dst]  # Return the minimum cost to reach the destination

# Main function
def main():
    # Input data
    n = 4
    src = 0
    dst = 3
    K = 1
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600],
               [2, 3, 200]]

    # Call the method to find the cheapest flight
    ans = CheapestFLight(n, flights, src, dst, K)

    # Output the result
    print(ans)

# Call the main function
if __name__ == "__main__":
    main()