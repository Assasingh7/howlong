def main(arr):
    st = []
    n = len(arr)
    res = []
    for i in range(n - 1, -1, -1):
        print("i",i)
        print("res",res)
        while st and st[-1] <= arr[i]:
            print("pop",st.pop())
        if not st:
            res.append(-1)
        else:
            res.append(st[-1])
        st.append(arr[i])
        print("st",st)
    return res
print(main([3, 2, 1]))