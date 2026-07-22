def main(arr, i, target, res, temp):
    if i==len(arr):
        if target == 0:
            res.append(temp[:])
        return
    if arr[i]<=target: 
        temp.append(arr[i])   
        main(arr, i, target-arr[i], res, temp)
        temp.pop()
    main(arr, i+1, target, res, temp)
    return
        
res = []
main([2,3,6,7], 0, 7, res, [])
print(res)