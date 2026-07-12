def larget_num(arr):
    n = len(arr)
    max_el = arr[0]
    for i in range(1, n):
        if arr[i]> max_el:
            max_el = arr[i]
    
    return max_el

if __name__ == "__main__":
    res = larget_num([2, 5, 1, 3, 0])
    print(res)