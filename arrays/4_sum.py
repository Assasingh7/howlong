# def main(arr, target):
#     n = len(arr)
#     ans = set()
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1, n):
#                 for l in range(k+1, n):
#                     if arr[i]+arr[j]+arr[k]+arr[l] == target:
#                         ans.add(tuple(sorted([arr[i], arr[j], arr[k], arr[l]])))

#     return [list(a) for a in ans]

def main(arr, target):
    n = len(arr)
    ans = set()
    for i in range(n):
        for j in range(i+1,n):
            seen = set()

            for k in range(j+1, n):
                # for l in range(k+1, n):
                rem = target - arr[i] - arr[j] - arr[k]
                if rem in seen:
                    ans.add(tuple(sorted([arr[i], arr[j], arr[k], rem])))
                seen.add(arr[k])
    return [list(a) for a in ans]
def mmain(arr, target):
    arr.sort()
    st = set()
    for i in range(len(arr)):
        if i>0 and arr[i] == arr[i-1]:
            continue
        for j in range(i+1, len(arr)):
            if j>i+1 and arr[j] == arr[j-1]:
                continue
            left, right = j+1, len(arr) - 1
            while left<right:
                summ = arr[i]+arr[j]+arr[left]+arr[right]
                if summ == target:
                    st.add(tuple([arr[i],arr[j],arr[left],arr[right]]))
                    while left<right and arr[left] == arr[left+1]:
                        left+=1
                    while left<right and arr[right] == arr[right-1]:
                        right-=1
                    left+=1
                    right-=1
                elif summ<target:
                    left+=1
                else:
                    right-=1
    return [list(s) for s in st]
                    

print(mmain([1,0,-1,0,-2,2], 0))