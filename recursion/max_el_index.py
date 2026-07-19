def main(arr, i, max_i):
    if i == len(arr):
        return max_i
    if arr[i]> arr[max_i]:
        max_i = i
    return main(arr, i+1, max_i)
a = main([1, 2, 7, 4, 5], 0, 0)
print(a)