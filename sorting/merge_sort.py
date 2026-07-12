    
def merge_sort(arr, low, high):
    n = len(arr)
    # low = 0
    # high = n - 1
    if low>=high:
        return
    mid = (low + high) // 2
    merge_sort(arr, low, mid)
    merge_sort(arr, mid+1, high)
    merge(arr, low, mid, high)
    
def merge(arr, low, mid, high):
    temp = []
    left = low
    right = mid + 1
    while left <=mid and right <= high:
        if arr[left]< arr[right]:
            temp.append(arr[left])
            left += 1
        else:
            temp.append(arr[right])
            right += 1 
    while left <= mid:
            temp.append(arr[left])
            left += 1
    while right <= high:
            temp.append(arr[right])
            right+=1
    for i in range(low, high+1):
        arr[i] = temp[i-low]

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    merge_sort(arr, 0, len(arr)-1)
    print(arr)
