def main(arr, i, j):
    if i>j:
        return True
    if arr[i]!=arr[j]:
        return False
    return main(arr, i+1, j-1)
a =main([1, 2, 8, 1], 0, 3)
print(a)