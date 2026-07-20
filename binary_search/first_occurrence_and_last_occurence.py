def first_occurence(arr, n, target):
    low = 0
    high = n - 1
    ans = -1
    while low<= high:
        mid = low+(high - low)//2
        if arr[mid] == target:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans
def lastt_occurence(arr, n, target):
    low = 0
    high = n - 1
    ans = -1
    while low<= high:
        mid = low+(high - low)//2
        if arr[mid] == target:
            ans = mid
            low = mid + 1
        else:
            high = mid - 1
    return ans

if __name__ == "__main__":
    print(lastt_occurence([2, 2 , 3 , 3 , 3 , 3 , 4], 7, 3))
    print(first_occurence([2, 2 , 3 , 3 , 3 , 3 , 4], 7, 3))