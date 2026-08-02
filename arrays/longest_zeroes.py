def main(arr, k):
    max_len = 0
    n = len(arr)
    for i in range(n):
        zero = 1
        for j in range(i, n):
            if arr[j] == 0:
                zero += 1
            if zero>k:
                break
            max_len = max(max_len, j-i+1)
    return max_len

def mainn(arr, k):
    left = 0
    max_len = 0
    zero = 0
    for right in range(len(arr)):
        if arr[right] == 0:
            zero+=1
        while zero>k:
            if arr[left] == 0:
                zero-=1
            left+=1
        max_len = max(max_len, right - left + 1)
    return max_len
 