def main(arr, i, sum, temp):
    if i==len(arr):
        temp.append(sum)
        return
    if sum<0:
        return
    main(arr, i+1, sum+arr[i], temp)

    main(arr, i+1, sum, temp)
    return

arr = [5,2,1]
n = len(arr)
temp = []
main(arr, 0, 0, temp)
temp.sort()
print(temp)
