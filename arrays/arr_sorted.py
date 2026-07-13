def main(arr):
    n = len(arr)
    for i in range(1, n):
        if arr[i] < arr[i-1]:
            return False
    return True
if __name__ == "__main__":
    is_sorted = main([1, 2, 3])
    print(is_sorted)
