def main(arr1, arr2, i, j, temp):
    n = len(arr1)
    m = len(arr2)
    # if i == n:
    #     # temp.extend[j:]
    #     for k in arr2[j:]:
    #         temp.append(k)
    #     return temp
    # if j == m:
    #     for k in arr1[i:]:
    #         temp.append(k)
    #     return temp
    if i == n:
        # temp.extend[j:]

        if j == m:
            return temp
        temp.append(arr2[j])
        return main(arr1, arr2, i, j+1, temp)
    if j == m:
        # temp.extend[j:]

        if i == n:
            return temp
        temp.append(arr1[i])
        return main(arr1, arr2, i+1, j, temp)
        
        

    if arr1[i]<=arr2[j]:
        temp.append(arr1[i])
        return main(arr1, arr2, i+1, j, temp)
        # main()
    else:
        temp.append(arr2[j])
        return main(arr1, arr2, i, j+1, temp)
    

print( main([1, 2, 3,4, 5], [6, 7, 8, 9], 0, 0, []))

    