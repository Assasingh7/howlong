def heapify(arr, n, i):

    while True:
        # Find children
        left = 2 * i + 1
        right = 2 * i + 2

        # Assume current is largest
        largest = i

        # Check left child
        if left < n and arr[left] > arr[largest]:
            largest = left

        # Check right child
        if right < n and arr[right] > arr[largest]:
            largest = right

        # Already a valid Max Heap
        if largest == i:
            break

        # Swap with larger child
        arr[i], arr[largest] = arr[largest], arr[i]

        # Continue downward
        i = largest
def heapSort(arr):

    n = len(arr)

    # Build Max Heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Move maximum to the end
    for i in range(n - 1, 0, -1):

        # Move root (maximum) to final position
        arr[0], arr[i] = arr[i], arr[0]

        # Heap size is now i
        # because arr[i] is already sorted
        heapify(arr, i, 0)

    return arr