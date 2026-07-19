def main(arr, i):
    if i == len(arr):
        return True
    if arr[i]<0:
        return False
    return main(arr, i+1)

if __name__ == "__main__":
    print(main([1, 2, 3, -4, 5], 0))
