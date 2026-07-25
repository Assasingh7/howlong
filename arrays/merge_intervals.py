def main(arr):
    arr.sort()
    i = 0
    ans = []

    while i< len(arr):
        strt = arr[i][0]
        end = arr[i][1]
        j = i+1
        while j<len(arr) and arr[j]<=end:
            end = max(end, arr[j])
            j+=1
        ans.append([strt, end])
        i = j
    return ans

def mainn(arr):
    ans = []
    for interval in arr:
        if not ans or ans[-1][1]<interval[0]:
            ans.append(interval)
        else:
            ans[-1][1] = max(ans[-1][1], interval[1])

    return ans