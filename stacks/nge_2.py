def main(arr):
    st = []
    res = [-1]*len(arr)

    for i in range(2*(len(arr))):
        
        curr = arr[i%(len(arr))]
        while st and curr>arr[st[-1]]:
            isx = st.pop()
            res[isx] = curr
        if i<len(arr):
            st.append(i)
    return res
        
