def main(arr, target):
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
    
if __name__ == "__main__":
    print(main([1,2,4,7], 6))