def brute(arr):
    st = set()
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == 0:
                    st.add(tuple(sorted([arr[i], arr[j], arr[k]])))
    
    return [list(ls) for ls in st]
def better(arr):
    st = set()
    for i in range(len(arr)):
        hs = set()
        for j in range(i+1, len(arr)):
            thir = -(arr[i]+arr[j])
            if thir in hs:
                st.add(tuple(sorted([arr[i], arr[j], thir])))
            hs.add(arr[j])
    return [list(ls) for ls in st]

def optimal(arr):
    arr.sort()
    ans = []
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue
        left = i+1
        right = len(arr)-1
        while left<right:
            tot = arr[i]+arr[left]+arr[right]
            if tot == 0:
                ans.append([arr[i], arr[left], arr[right]])
                left+=1
                right-=1
                while left<right and arr[left] == arr[left-1]:
                    left+=1
                while right<len(arr)-1 and left<right and arr[right] == arr[right+1]:
                    right-=1
            elif tot<0:
                left+=1
            else:
                right-=1
    return ans


print(optimal([-1,0,1,2,-1,-4]))