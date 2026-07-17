def main(arr, k):
    n = len(arr)
    low = 0
    high = n-1
    while low<=high:
        mid = low+(high-low)//2
        if arr[mid] == k:
            return mid
        if arr[low]<=arr[mid]:
            if arr[low]<=k<arr[mid]:
                high = mid - 1
            else:
                low = mid+1
        else:
            if arr[mid]<k<=arr[high]:
                low = mid+1
            else:
                high = mid - 1
    
    return -1

if __name__ == "__main__":
    print(main([4, 5, 6, 7, 0, 1, 2], 0))