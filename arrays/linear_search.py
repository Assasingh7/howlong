def main(arr, n):
    l = len(arr)
    for i in range(l):
        if arr[i] == n:
            return i
    return -1
if __name__ == "__main__":
    print(main([1, 2, 3, 4, 5], 3))
