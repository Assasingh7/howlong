def main(arr):
    n = len(arr)
    j=0
    for i in range(1, n):
        if arr[i] != arr[j]:
            j+=1
            arr[j] = arr[i]
    return j+1

