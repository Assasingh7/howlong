def main_c(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1
    while(low<=high):
        mid = low + (high - low) // 2
        if arr[mid]>=target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans

def main(arr, target):
    low = 0
    high = len(arr) - 1
    ans = -1
    while(low<=high):
        mid = low + (high - low) // 2
        if arr[mid]<=target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

if __name__ == "__main__":
    # ceil floor
    print(main_c([3, 4, 4, 7, 8, 10], 5), main([3, 4, 4, 7, 8, 10], 5))