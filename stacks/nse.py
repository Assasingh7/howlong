def main(arr):
    st = []
    st.append()
    res = []
    for i in range(len(arr)):
        while st and arr[st[-1]]>arr[i]:
            idx = st.pop()
            res[idx] = arr[i]

        st.append(arr[i])
    return res