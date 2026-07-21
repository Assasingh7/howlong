def main(arr,i, k):
    if i == len(arr):
        if k ==0:
            return True
        return False
    if k<0:
        return False
    return main(arr, i+1, k-arr[i]) or main(arr, i+1, k)
    

print(main([4, 3, 9, 2], 0, 10))