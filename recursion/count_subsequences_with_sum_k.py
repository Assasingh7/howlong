def main(arr,i, k):
    if i == len(arr):
        if k ==0:
            return 1
        
        return 0
    if k<0:
        return 0
 
    return main(arr, i+1, k-arr[i]) + main(arr, i+1, k)
    

print(main([1, 2,3], 0, 3))
