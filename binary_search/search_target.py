def bs(arr, target):
    low = 0
    high = len(arr) - 1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid] == target:
            return mid
        elif arr[mid]> target:
            high = mid - 1
        else:
            low = mid+1
    return -1
def bs_rec(arr, target, low, high):
    if low>high:
        return -1
    mid = low + (high - low) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid]>target:
        return bs_rec(arr, target, low, mid - 1)
    else:
        return bs_rec(arr, target, mid+1, high)
if __name__ == "__main__":
    print(bs_rec([3, 4, 6, 7, 9, 12, 16, 17], 6, 0, 8-1))