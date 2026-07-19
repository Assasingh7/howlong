def main(arr1, arr2, i):
    if len(arr1) != len(arr2):
        return False
    if i == len(arr1):
        return True
    if arr1[i] != arr2[i]:
        return False
    return main(arr1, arr2, i+1)
a = main([1, 2, 3,4], [1, 2, 4, 4], 0)
print(a)