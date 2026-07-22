def main(arr, i, target, temp, res):
    if target == 0:
        res.append(temp[:])
        return
    for ind in range(i, len(arr)):
        if ind>i and arr[ind] == arr[ind-1]:
            continue
        if arr[ind]>target:
            break
        temp.append(arr[ind])
        main(arr, ind+1, target-arr[ind], temp, res)
        temp.pop()


res = []
arr = [10,1,2,7,6,1,5]
arr.sort()
main(arr, 0, 8, [], res)
print(res)