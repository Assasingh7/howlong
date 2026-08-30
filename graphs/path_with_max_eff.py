import heapq

# Method to calculate the minimum effort path using Dijkstra's algorithm
def MinimumEffort(heights):

    # Get the grid size
    n = len(heights)
    m = len(heights[0])

    # Create a distance matrix, initialized with a large value (unvisited)
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0  # Distance for the source cell (0, 0) is 0

    # Create a priority queue for Dijkstra's algorithm
    pq = [(0, 0, 0)]  # Push source cell with distance 0

    # Define the possible directions (up, right, down, left)
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    # Start the Dijkstra algorithm
    while pq:
        diff, r, c = heapq.heappop(pq)

        # If we reach the destination cell, return the current effort
        if r == n - 1 and c == m - 1:
            return diff

        # Check all 4 possible adjacent cells
        for i in range(4):
            newr, newc = r + dr[i], c + dc[i]

            # Check if the new cell is within bounds
            if 0 <= newr < n and 0 <= newc < m:
                # Calculate the effort required to move to the new cell
                newEffort = max(abs(heights[r][c] - heights[newr][newc]), diff)

                # If the calculated effort is less, update and push to the queue
                if newEffort < dist[newr][newc]:
                    dist[newr][newc] = newEffort
                    heapq.heappush(pq, (newEffort, newr, newc))

    return 0  # If unreachable (although it should not reach here)

# Main function
def main():
    # Input data
    heights = [
        [1, 2, 2], 
        [3, 8, 2], 
        [5, 3, 5]
    ]

    # Find the minimum effort path
    res = MinimumEffort(heights)

    # Output the result
    print(res)

# Call the main function
if __name__ == "__main__":
    main()