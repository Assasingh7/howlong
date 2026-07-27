def main(arr):
    n = len(arr) - 1
    low = 0
    high = n - 1
    while low<high:
        mid = low+(high-low)//2
        if arr[mid]>arr[high]:
            low = mid+1
        else:
            high = mid
    return arr[low]
print(main([4,5,6,7,0,1,2,3]))
