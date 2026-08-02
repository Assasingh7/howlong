def main(arr):
    low = 0
    high = len(arr) - 1
    while low<high:
        mid = low + (high - low) //2
        if arr[mid]>arr[high]:
            low = mid+1
        else:
            high = mid - 1
    return low