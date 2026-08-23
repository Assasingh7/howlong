def heapify(arr, i, n):

    while True:

        # Find children
        left = 2 * i + 1
        right = 2 * i + 2

        # Assume current node is smallest
        smallest = i

        # Check left child
        if left < n and arr[left] < arr[smallest]:
            smallest = left

        # Check right child
        if right < n and arr[right] < arr[smallest]:
            smallest = right

        # Current node is already smallest
        if smallest == i:
            break

        # Swap with smaller child
        arr[i], arr[smallest] = arr[smallest], arr[i]

        # Continue downward
        i = smallest
def buildMinHeap(arr):

    n = len(arr)

    # Last non-leaf node
    start = n // 2 - 1

    # Heapify every non-leaf node
    # from right to left
    for i in range(start, -1, -1):

        heapify(arr, i, n)

    return arr