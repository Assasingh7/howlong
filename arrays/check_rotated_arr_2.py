def main(arr, target):
    n = len(arr)
    low = 0
    high = n - 1
    while low<=high:
        mid = low+(high-low)//2

        if arr[mid] == target:
            return True
        elif arr[low] == arr[mid] and arr[mid] == arr[high]:
            low+=1
            high-=1
        elif arr[mid]<=arr[high]:
            if arr[mid]<target and target<=arr[high]:
                low = mid+1
            else:
                high = mid-1
        else:
            if arr[low]<=target and target<arr[mid]:
                high = mid - 1
            else:
                low = mid+1
    return False
