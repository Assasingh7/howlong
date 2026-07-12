def insertion_sort(arr):
    n = len(arr)
    for i in range(n-1):
        min = i
        for j in range(i+1, n):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr

if __name__ == "__main__":
    arr = [5, 4, 3, 2, 1]
    sorted_arr = insertion_sort(arr)
    print(sorted_arr)
