def main(arr, i, largest, second_largest):
    if i ==len(arr):
        # print(second_largest)
        return second_largest

    if arr[i]> largest:
        second_largest = largest
        largest = arr[i]
    if arr[i]> second_largest and arr[i]!=largest:
        second_largest = arr[i]

    return main(arr, i+1, largest, second_largest)
    

if __name__ == "__main__":
    print(main([1, 2, 3, 4, 5], 0, float('-inf'), 0))