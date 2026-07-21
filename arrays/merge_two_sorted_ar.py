def main(arr1,arr2, n, m):
    i = n-1
    j = m-1
    k = m+n-1
    while i>=0 and j>=0:
        if arr1[i]>= arr2[j]:

            arr1[k] = arr1[i]
            i-=1
        else:
            arr1[k] = arr2[j]
            j-=1
        k-=1
    while j>=0:
        arr1[k] = arr2[j]
        k-=1
        j-=1
    
    
if __name__ == "__main__":
    nums1 = [1, 3, 5, 0, 0, 0]
    nums2 = [2, 4, 6]
    m, n = 3, 3
    main(nums1, nums2, m, n)
    print(nums1)
