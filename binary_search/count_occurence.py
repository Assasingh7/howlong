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
def main(arr, x):
    n = len(arr)
    f = first_occurence(arr, n, x)
    print(f)
    l = lastt_occurence(arr, n, x)
    print(l)
    return l - f +1 if f>-1 else 0

if __name__ == "__main__":
    arr = [2, 2 , 3 , 3 , 3 , 3 , 4]
    n = len(arr)
    res  = main(arr,  5)
    print(res)