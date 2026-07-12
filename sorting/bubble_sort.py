def main(arr):
    n = len(arr)
    for i in range(n-1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

if __name__ == "__main__":
    sorted_arr = main([5, 4, 3, 2, 1])
    print(sorted_arr)