def msin(arr):
    n = len(arr)
    res = []
    cnt_0=0
    cnt_1=0
    cnt_2=0
    for i in range(n):
        if arr[i] == 0:
            cnt_0+=1
        elif arr[i] == 1:
            cnt_1+=1
        else:
            cnt_2+=1
    while cnt_0 !=0:
        res.append(0)
        cnt_0 -=1
    while cnt_1 !=1:
        res.append(1)
        cnt_1 -=1
    while cnt_2 !=0:
        res.append(2)
        cnt_2 -=1
    return res

def swap(arr, a, b):
    arr[a], arr[b] = arr[b], arr[a]
    
def main(arr):
    n = len(arr)
    low = 0
    mid = 0
    high = n - 1
    while mid <= high:
        if arr[mid] == 0:
            swap(arr, low, mid)
            mid+=1
            low+=1
        elif arr[mid] == 1:
            mid+=1
        else:
            swap(arr, mid, high)
            high-=1
    return arr


if __name__ == "__main__":
    print(main([1, 0, 2, 1, 0]))
    