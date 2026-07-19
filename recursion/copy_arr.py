def main(arr, temp, i):
    if i==len(arr):
        return temp
    temp.append(arr[i])
    return main(arr, temp, i+1)
print(main([1,2], [], 0))
